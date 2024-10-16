from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    introduction = models.TextField(default="This is the main introduction")
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
  
    def __str__(self):
        return self.title
