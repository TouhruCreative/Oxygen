from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models

"""
Model architecture

User
 ├── username (CharField)
 ├── email (EmailField)
 ├── password (CharField)
 ├── is_seller (BooleanField)
 ├── is_active (BooleanField)
 └── date_joined (DateTimeField) mb

Profile (опционально)
 ├── user (OneToOne → User)
 ├── avatar (ImageField)
 ├── phone (CharField)
 └── address (TextField)

"""

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("moderator", "Moderator"),
        ("client", "Client"),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    phone = models.CharField(max_length=50, unique=True)
    address = models.TextField()