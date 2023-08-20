# blog/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Comment, BlogPost
from .serializers import CommentSerializer
from .serializers import BlogPostSerializer
from django.shortcuts import render


class CreateBlogPost(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateComment(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id, format=None):
        try:
            blog_post = BlogPost.objects.get(pk=post_id)
        except BlogPost.DoesNotExist:
            return Response({'error': 'Blog post not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, blog_post=blog_post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ListBlogPosts(APIView):
    def get(self, request, format=None):
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)

class ListComments(APIView):
    def get(self, request, post_id, format=None):
        try:
            blog_post = BlogPost.objects.get(pk=post_id)
        except BlogPost.DoesNotExist:
            return Response({'error': 'Blog post not found'}, status=status.HTTP_404_NOT_FOUND)

        comments = blog_post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class UpdateBlogPost(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, post_id, format=None):
        try:
            blog_post = BlogPost.objects.get(pk=post_id)
        except BlogPost.DoesNotExist:
            return Response({'error': 'Blog post not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if blog_post.author != request.user:
            return Response({'error': 'You do not have permission to update this post'}, status=status.HTTP_403_FORBIDDEN)

        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
