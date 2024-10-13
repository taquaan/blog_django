from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
  
    def __str__(self):
        return self.title
