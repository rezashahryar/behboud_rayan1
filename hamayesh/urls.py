from django.urls import path, include


app_name = 'hamayesh'
urlpatterns = [
    path('api/v1/', include('hamayesh.api.v1.urls')),
]