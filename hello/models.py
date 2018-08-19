from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=False, db_index=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Place(models.Model):
    created = models.DateTimeField('date created', auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=False,  db_index=True)
    country = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, null=True,  blank=True)
    postcode = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    longditude = models.FloatField(blank=True)
    latitude = models.FloatField(blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=2000, blank=True)

class Label(models.Model):
    created = models.DateTimeField('date created', auto_now_add=True)
    label = models.CharField(max_length=30, blank=True)

class PlaceLabelLink(models.Model):
    created = models.DateTimeField('date created', auto_now_add=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
