from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    introduction = models.TextField(default="This is the main introduction")
    categories = models.ManyToManyField(Categories)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
  
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.comment_id} by {self.user}"

