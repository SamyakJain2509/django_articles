from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    pic = models.ImageField(upload_to='pics', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} profile'