from rest_framework import serializers
from ..models import Blog
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = "__all__"
    
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["username", "email", "password"]