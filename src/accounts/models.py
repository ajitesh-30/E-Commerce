from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,	
)

class UserManager(BaseUserManager):
	pass 
class CustomUser(AbstractBaseUser):
	email  = models.EmailField(max_length=255,unique=True)
	active = models.BooleanField(default=True) #can login
	staff  = models.BooleanField(default=False) #staff user non superuser
	admin  = models.BooleanField(default=False) #superuser

	USERNAME_FIELD  = 'email'
	REQUIRED_FIELDS = []
 	
 	objects =  UserManager()
	def __str__(self):
		return

	def get_full_name(self):
		return

class Profile(models.Model):
	user = models.OnetoOneField(User)

class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
