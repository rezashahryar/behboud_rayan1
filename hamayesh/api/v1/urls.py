from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

app_name = 'api-v1'

router = DefaultRouter()
router.register('h', views.HamayeshViewSet, basename='hamayesh')

urlpatterns = [
    path('register/', views.RegisterHamayesh.as_view(), name='hamayesh_register'),
    path('', include(router.urls)),
]
