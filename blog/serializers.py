# blog/serializers.py

from rest_framework import serializers
from .models import BlogPost
from .models import Comment

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
