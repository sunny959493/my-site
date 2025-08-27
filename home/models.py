from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics/')
    place=models.CharField(max_length=200)
    date=models.CharField(max_length=20)

class user_uploads(models.Model):
    place=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics/')
    description=models.CharField(max_length=200)

class favourites(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(user_uploads, on_delete=models.CASCADE)