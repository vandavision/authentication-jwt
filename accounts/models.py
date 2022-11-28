from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=255, unique=True)
	vrify_email = models.BooleanField(default=False)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=250)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self):
		return self.email

	@property
	def is_staff(self):
		return self.is_admin

	def tokens(self):
		return ''
