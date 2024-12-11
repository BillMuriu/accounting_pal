from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # User roles
    ROLE_CHOICES = [
        ('principal', 'School Principal'),
        ('secretary', 'Secretary'),
        ('it_admin', 'IT Admin'),
        ('other', 'Others'),
    ]

    # Adding fields
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='other',
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    is_verified = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.email
