from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User

# class User(AbstractBaseUser):
#     username = None
#
#     name = models.CharField('Name', max_length=30)
#     city = models.CharField('City', max_length=30)
#     email = models.CharField('Email', max_length=30, unique=True)
#     password = models.TextField('Password', max_length=30)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('Name', 'City', 'Email', 'Password')
#     def __str__(self):
#         return self.email

# class UserA(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField('Name', max_length=30)
    # city = models.CharField('City', max_length=30)
    # email = models.CharField('Email', max_length=30, unique=True)
    # password = models.TextField('Password', max_length=30)
