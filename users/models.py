
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
class CustomUser(AbstractUser):
    STATUS = (
        ('subscriber', 'subscriber'),
        ('regular', 'regular'),
        ('moderator', 'moderator')
    )
    picture = models.ImageField(default='images/profile.jpeg', upload_to="images/profile_pics")
    # picture = models.CharField (max_length=50, choices= STATUS, default='regular')

    email = models.EmailField(unique=True)
    status = models.CharField (max_length=50, choices= STATUS, default='regular')
    description = models.TextField('Description', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)
        if self.picture:
            img = Image.open(self.picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.picture.path)
    
        
