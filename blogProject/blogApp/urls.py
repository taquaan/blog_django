from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('create_blog/', views.create_blog_view, name="create"),
    path('blog_list/', views.blog_list_view, name="read"),
    path('update_blog/<int:id>', views.update_blog_view, name="update"),
    path('delete_blog/<int:id>', views.delete_blog_view, name="delete"),
]