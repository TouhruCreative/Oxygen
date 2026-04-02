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
 └── date_joined (DateTimeField)

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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email