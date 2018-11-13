from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser	
)

class CustomUser(AbstractBaseUser):
	email  = models.EmailField(max_length=255,unique=True)
	active = models.BooleanField(default=True)
	staff  = models.BooleanField(default=False)
	admin  = models.BooleanField(default=False)

	USERNAME_FIELD  = 'email'
	REQUIRED_FIELDS = []

	def __str__(self):
		return

	def get_full_name(self):
		return
	

class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email