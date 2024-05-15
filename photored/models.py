from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import secrets
# from .paystack import Paystack


class UserProfile(models.Model):
    image = models.ImageField()
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username

from django.db import models

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Graphics', 'Graphics'),
        ('3D', '3D'),
        ('2D', '2D'),
        ('Videos', 'Videos'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Graphics')  # Example default value
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class VideoPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='video_post')
    # Add additional fields specific to VideoPost model

class GraphicsPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='graphics_post')
class thDPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='thDPost')
class twDPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='twDPost')

# Add similar models for other categories (3D, 2D, etc.)
