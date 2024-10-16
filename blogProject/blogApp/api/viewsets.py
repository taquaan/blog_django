from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import BlogSerializer, UserSerializer
from ..models import Blog
from django.contrib.auth.models import User

# GET/POST BLOGS
class ListCreateBlogView(ListCreateAPIView):
    model = Blog
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Blog.objects.all()
    
    # HANDLE BLOG CREATE
    def create(self, request, *args, **kwargs):
        serializer = BlogSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'New Blog created successfully'
            }, status=status.HTTP_201_CREATED)
        return JsonResponse({
            'message': 'Invalid Blog credentials. Please try again'
        }, status=status.HTTP_400_BAD_REQUEST)
        
# UPDATE/DELETE BLOG
class UpdateDeleteBlogView(RetrieveUpdateDestroyAPIView):
    model = Blog
    serializer_class = BlogSerializer
    lookup_field = "blog_id"
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Blog.objects.all()
    
    # HANDLE BLOG UPDATE
    def put(self, request, *args, **kwargs):
        blog = self.get_object() 
        serializer = BlogSerializer(blog, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Update Blog Successfully'
            }, status = status.HTTP_200_OK)
        return JsonResponse({
            'message': 'Update Blog Unsuccessful'
        }, status = status.HTTP_400_BAD_REQUEST)
        
    # HANDLE BLOG DELETE
    def delete(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.delete()
        return JsonResponse({
            'message': 'Blog Deleted Successfully'
        }, status=status.HTTP_200_OK)
        
# GET/POST USERS
class ListCreateUserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        return User.objects.all()
    
    
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        
        if serializer.is_valid():
            return JsonResponse({"message": "User created successfully"}, status = status.HTTP_200_OK)
        return JsonResponse({"message": "Invaid credentials"}, status = status.HTTP_400_BAD_REQUEST)

# UPDATE/DELETE USER
class UpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = "id"
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        return User.objects.all()
    
    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserSerializer(user, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'User updated successfully'}, status = status.HTTP_200_OK)
        return JsonResponse({'message': 'Invaid User Credentials'}, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status = status.HTTP_200_OK)
        