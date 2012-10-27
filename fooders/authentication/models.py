from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_image_big = models.ImageField(upload_to='profile_images')
    profile_image_normal = models.ImageField(upload_to='profile_images')
    profile_image_small = models.ImageField(upload_to='profile_images')


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
