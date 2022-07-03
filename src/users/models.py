from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=True, default=None)
    birth_date = models.DateField(null=True, blank=True, default=None)
    location = models.CharField(max_length=30, blank=True, default=None)
    favorite_words = models.CharField(max_length=50, blank=True, default=None)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()