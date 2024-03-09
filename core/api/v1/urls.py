from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]