from django.db import models

class CustomUser(models.Model):
    # User roles
    ROLE_CHOICES = [
        ('principal', 'School Principal'),
        ('secretary', 'Secretary'),
        ('it_admin', 'IT Admin'),
        ('other', 'Others'),
    ]

    # Adding fields
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
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
