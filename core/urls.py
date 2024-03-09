from django.urls import path, include


app_name = 'core'
urlpatterns = [
    path('api/v1/', include('core.api.v1.urls')),
]