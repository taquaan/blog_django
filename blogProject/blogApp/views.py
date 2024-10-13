from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required

# HOME VIEW
def home_view(request):
    return render(request, 'public/home.html')


# BLOG LIST VIEW
def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'public/blog_list.html', {'blogs': blogs})


# LOGIN VIEW
def login_view(request):
    form = LoginForm()
    loginErr = "Invalid login credentials. Please try again."

    if request.method == "POST":
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


# REGISTER FORM
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


# CREATE BLOG VIEW
@login_required
def create_blog_view(request):
    form = BlogForm()
    createBlogErr = 'Created blog failed. Please try again'
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        
        # Check which button was pressed
        action = request.POST.get('action')
        
        if action == 'submit': 
            if form.is_valid():
                blog = form.save(commit=False)
                blog.author = request.user
                blog.status = "published"
                blog.save()
                return redirect('home')
            else:
                return render(request, 'private/create_blog.html', {"form": form, "error": createBlogErr})
            
        elif action == "save":
            if form.is_valid():
                blog = form.save(commit=False)
                blog.author = request.user
                blog.statud = "draft"  
                blog.save()
                return redirect('blog_list')
            else:
                return render(request, 'private/create_blog.html', {"form": form, "error": createBlogErr})
            
        elif action == "cancel":
            return redirect("blog_list")
        
        return render(request, 'private/create_blog.html', {"form": form, "error": createBlogErr})
        
    return render(request, 'private/create_blog.html', {'form': form})


# UPDATE BLOG VIEW
@login_required
def update_blog_view(request, id):
    updateBlogErr = 'Updated blog failed. Please try again'

    # Initiate a new form with blog's data
    blog = Blog.objects.get(blog_id=id)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if (form.is_valid()):
            form.save()
            return redirect('home')
        
        else:
            return render(request, 'private/update_blog.html', {'form': form, 'error': updateBlogErr})
        
    return render(request, 'private/update_blog.html', {'form': form})


# DELETE BLOG VIEW
@login_required
def delete_blog_view(request, id):
    blog = Blog.objects.get(blog_id=id)
            
    if request.method == "POST":
        blog.delete()
        return redirect('blog_list')
    
    return render(request, 'private/delete_blog.html', {'blog': blog})