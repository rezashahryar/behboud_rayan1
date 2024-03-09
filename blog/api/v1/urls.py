from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

app_name = 'api-v1'

router = DefaultRouter()
router.register('post', views.PostViewSet, basename='post')
router.register('category', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]
