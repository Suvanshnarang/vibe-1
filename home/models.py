from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Detail(models.Model):
    username = models.CharField(max_length=100, default="")
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.username}'