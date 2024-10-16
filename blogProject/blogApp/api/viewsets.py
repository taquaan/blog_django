from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import BlogSerializer
from ..models import Blog

# API
# Get all blogs - Create a new blog
class ListCreateBlogView(ListCreateAPIView):
    model = Blog
    serializer_class = BlogSerializer
    
    # Specify the model instance to query
    def get_queryset(self):
        return Blog.objects.all()
    
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
        

# Update a blog - delete a blog
class UpdateDeleteBlogView(RetrieveUpdateDestroyAPIView):
    model = Blog
    serializer_class = BlogSerializer
    lookup_field = "blog_id"
    
    def get_queryset(self):
        return Blog.objects.all()
    
    # HANDLE UPDATE
    def put(self, request, *args, **kwargs):
        # Get the blog about to get updated
        blog = self.get_object() 
        serializer = BlogSerializer(blog, data=request.data)
        # Update that blog with the request data
        
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse({
                'message': 'Update Blog Successfully'
            }, status = status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Blog Unsuccessful'
        }, status = status.HTTP_400_BAD_REQUEST)
        
    # HANDLE DELETE
    def delete(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.delete()
        
        return JsonResponse({
            'message': 'Blog Deleted Successfully'
        }, status=status.HTTP_200_OK)