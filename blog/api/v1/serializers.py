from rest_framework import serializers
from blog.models import Post, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tag = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = [
            'title', 'description', 'image', 'category', 'tag',
            'author', 'published_date', 'datetime_created', 'status'
        ]