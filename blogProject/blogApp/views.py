from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, BlogForm, CommentForm
from .models import Blog, Comment, Categories
from django.contrib.auth.decorators import login_required

# HOME VIEW
def home_view(request):
    recentBlogs = Blog.objects.filter(status="published").order_by("-created_at")[:3]
    previewBlogs = Blog.objects.filter(status="published")[:25]
    return render(request, 'public/home.html', {"recentBlogs": recentBlogs, "previewBlogs": previewBlogs})

# BLOG LIST VIEW
def blog_list_view(request):
    blogs = Blog.objects.filter(status="published").order_by("-created_at")
    return render(request, 'public/blog_list.html', {'blogs': blogs})

# BLOG DETAIL VIEW
def blog_detail_view(request, id):
    blog = Blog.objects.get(blog_id = id, status="published")
    comments = Comment.objects.filter(blog=blog)
    comment_form = CommentForm()
    categories = blog.categories.all()

    # HANDLE COMMENT CREATION
    if request.method == "POST":
        if "create_comment" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.blog = blog
                new_comment.author = request.user
                new_comment.save()
                return redirect('blog_detail', id=blog.blog_id)
        elif "delete_comment" in request.POST:
            comment_id = request.POST.get('comment_id')
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return redirect('blog_detail', blog.blog_id)

    return render(request, 'public/blog_detail.html', {"blog": blog, "comments": comments, "comment_form": comment_form, "categories": categories})

# MY BLOG VIEW
@login_required
def my_blog_view(request):
    publishedBlogs = Blog.objects.filter(author = request.user, status = "published")
    draftBlogs = Blog.objects.filter(author = request.user, status = "draft")
    return render(request, 'private/my_blog.html', {'publishedBlogs': publishedBlogs, 'draftBlogs': draftBlogs})

# LOGIN VIEW
def login_view(request):
    form = LoginForm()
    loginErr = "Invalid login credentials. Please try again."

    if request.method == "POST":
        # Handle Logout function
        action = request.POST.get('action')
        if action == "logout":
            logout(request)
            return redirect(request.path)
          
        form = LoginForm(request.POST)
    
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            # Check if a user exists with this email
            try:
                user = User.objects.get(email=email)
                username = user.username
            except User.DoesNotExist:
                return render(request, 'accounts/login.html', {'form': form, 'error': loginErr})

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'form': form, 'error': loginErr})

        # If form is invalid    
        else:
            return render(request, 'accounts/login.html', {'form': form, 'error': loginErr})
    
    return render(request, 'accounts/login.html', {'form': form})

# REGISTER VIEW
def register_view(request):
    form = RegisterForm()
    regisErr = "Invalid credentials. Please try again."

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'accounts/register.html', {'form': form, 'error': regisErr})
    
    return render(request, 'accounts/register.html', {'form': form})

# SEARCH VIEW
def search_view(request):
    blogs = Blog.objects.filter(status="published").order_by("-created_at")[:15]
    if request.method == "POST":
        query = request.POST['search_query']
        blogs = Blog.objects.filter(status="published",title__contains=query)[:15]
        return render(request, "public/search_view.html", {"blogs": blogs})
    return render(request, "public/search_view.html", {"blogs": blogs})

# CREATE BLOG VIEW
@login_required
def create_blog_view(request):
    form = BlogForm()
    categories = Categories.objects.all()
    createBlogErr = 'Created blog failed. Please try again'
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        
        updateCreate(request, form, createBlogErr, categories)
        
    return render(request, 'private/create_blog.html', {'form': form, "categories": categories})


# UPDATE BLOG VIEW
@login_required
def update_blog_view(request, id):
    updateBlogErr = 'Updated blog failed. Please try again'

    # Initiate a new form with blog's data
    blog = Blog.objects.get(blog_id=id)
    categories = Categories.objects.all()
    chosen_categories = blog.categories.all()
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        updateCreate(request, form, updateBlogErr, categories, chosen_categories)
        
    return render(request, 'private/create_blog.html', {'form': form, 'categories': categories, 'chosen_categories': chosen_categories})

# CATEGORY FILTER VIEW
def category_view(request, id):
    category = Categories.objects.get(id=id)
    blogs = Blog.objects.filter(categories = category)
    print(blogs)
    return render(request, 'public/blog_cate.html', {"category": category, "blogs": blogs})

# METHOD TO HANDLE UPDATE CREATE
def updateCreate(request, form, error, categories=None, chosen_categories=None):
    # Check which button was pressed
        action = request.POST.get('action')
        
        if action == 'submit': 
            if form.is_valid():
                selected_cate = form.cleaned_data.get('categories')
                filtered_cate = list(set(selected_cate))
                blog = form.save(commit=False)
                blog.author = request.user
                blog.status = "published"
                blog.save()
                blog.categories.set(filtered_cate)
                return redirect('home')
            else:
                return render(request, 'private/create_blog.html', {"form": form, "error": error})
            
        elif action == "save":
            if form.is_valid():
                selected_cate = form.cleaned_data.get('categories')
                filtered_cate = list(set(selected_cate))
                blog = form.save(commit=False)
                blog.author = request.user
                blog.status = "draft"  
                blog.save()
                blog.categories.set(filtered_cate)
                return redirect('blog_list')
            else:
                return render(request, 'private/create_blog.html', {"form": form, "error": error})
            
        elif action == "cancel":
            return redirect("my_blog")
        
        elif action == "delete":
            form.instance.delete()
            return redirect("my_blog")
        
        return render(request, 'private/create_blog.html', {"form": form, "error": error, "categories": categories, "chosen_categories": chosen_categories})