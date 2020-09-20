from django.shortcuts import render
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer
# Create your views here.



class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blog posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
