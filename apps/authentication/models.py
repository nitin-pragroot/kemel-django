# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.db import models
from django.conf import settings


USER_ROLES = tuple((usr,usr) for usr in settings.USER_ROLES)


class User(AbstractBaseUser, PermissionsMixin):
    """ 
        User
    """
    username        = models.CharField(max_length=50,unique=True)
    email           = models.EmailField(unique=True)
    role            = models.CharField(max_length=20, choices=USER_ROLES, default='USER')
    phone           = models.CharField(max_length=20, default='',  blank=True)
    fullname        = models.CharField(max_length=50, default='',  blank=True)
    address         = models.TextField(default='',    blank=True)
    zipcode         = models.CharField(max_length=10, default='',  blank=True)
    bio             = models.TextField(default='',    blank=True)
    image           = models.ImageField(default="/images/user/avatar-2.jpg", blank=True)

    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
