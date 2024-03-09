from rest_framework.viewsets import ModelViewSet
from blog.models import Post, Category
from .serializers import PostSerializer, CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializer