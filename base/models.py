from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='files/books')


    def __str__(self):
        return self.bookname


class Music(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    musicname = models.CharField(max_length=200)
    musicpath = models.FileField(upload_to='files/music')

    def __str__(self):
        return self.musicname
