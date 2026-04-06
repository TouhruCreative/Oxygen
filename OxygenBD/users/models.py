from django.contrib.auth.models import AbstractUser
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

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin","Admin"),
        ("moderator","Moderator"),
        ("client","Client"),
    )

    username = models.CharField(blank=True,null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    phone = models.CharField(max_length=50, unique=True)
    address = models.TextField()