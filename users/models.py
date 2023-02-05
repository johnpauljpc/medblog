
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    STATUS = (
        ('subscriber', 'subscriber'),
        ('regular', 'regular'),
        ('moderator', 'moderator')
    )
    email = models.EmailField(unique=True)
    status = models.CharField (max_length=50, choices= STATUS, default='regular')
    decription = models.TextField('Description', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username
