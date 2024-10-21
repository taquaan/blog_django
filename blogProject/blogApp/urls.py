from django.urls import path
from . import views
from .api import viewsets

urlpatterns = [
    # Template URLs
    path('', views.home_view, name="home"),
    path('accounts/login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('create_blog/', views.create_blog_view, name="create"),
    path('blog_list/', views.blog_list_view, name="blog_list"),
    path("my_blog/", views.my_blog_view , name="my_blog"),
    path('blog_detail/<int:id>', views.blog_detail_view, name="blog_detail"),
    path('update_blog/<int:id>', views.update_blog_view, name="update"),
    path('search/', views.search_view, name="search"),
    
    # API URLs
    path('blogs/', viewsets.ListCreateBlogView.as_view(), name="create_get_blogs"),
    path('blogs/<int:blog_id>', viewsets.UpdateDeleteBlogView.as_view(), name="update_delete_blog"),
    
    # API USER URLs
    path("users/", viewsets.ListCreateUserView.as_view(), name="create_get_users"),
    path("users/<int:id>", viewsets.UpdateDeleteUserView.as_view(), name="update_delete_user"),
]