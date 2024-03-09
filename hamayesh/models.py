from django.db import models
from django.conf import settings
from django_jalali.db.models import jDateTimeField
# Create your models here.


class Hamayesh(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hamayeshat')
    date_of_hamayesh = jDateTimeField()
    location = models.TextField()
    image = models.ImageField(upload_to='hamayeshat/', null=True)

    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


class ParticipantHamayesh(models.Model):
    hamayesh = models.ForeignKey(Hamayesh, on_delete=models.CASCADE, related_name='participants')
    email = models.EmailField()
    mobile_number = models.CharField(max_length=11)
    full_name = models.CharField(max_length=255)