# main_fns_app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')

    def __str__(self):
        return f'{self.username} ({self.role})'
