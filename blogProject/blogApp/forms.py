from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Blog

# REGISTER FORM
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True, label="Username")
    email = forms.EmailField(max_length=75, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Password Confirm', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_cfr = cleaned_data.get("password_confirm")
        
        if password and password_cfr and password != password_cfr:
            raise ValidationError("Passwords do not match")
        return cleaned_data
    
# LOGIN FORM
class LoginForm(forms.ModelForm):
    email = forms.EmailField(max_length=75, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)

    class Meta:
        model = User
        fields = ['email', 'password']

# BLOG FORM
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']