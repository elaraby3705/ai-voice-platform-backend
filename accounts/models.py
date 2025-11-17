from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    """Custom User manager That uses email instead of username """
    use_in_migration =True

    def _create_user(self,email , password, **extra_fields):
        if not email:
            raise ValueError("Email is required ")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
        if extra_fields.get("is_staff") is not True:
            raise ValueError ("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have is_superuser=True.")

        return self._create_user(email,password , **extra_fields)



class User(AbstractUser):
    """Custom user model using email as unique identifier """
    username= None # to remove username field entirely

    USERNAME_FIELD= "email"
    REQUIRED_FIELDS=[]

    object =UserManager()

    def __str__(self):
        return self.email

