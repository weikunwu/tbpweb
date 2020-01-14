from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Profile(models.Model):
    def __init__(self,user):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        first_name = models.CharField(max_length=100, blank=True)
        last_name = models.CharField(max_length=100, blank=True)
        email = models.EmailField(max_length=150)

class StudentProfile(Profile):
    def __init__(self,user):
        super().__init__(user)
        self.preferred_name = models.CharField(max_length=100, blank=True)
        self.birth_date = models.DateTimeField(default=datetime(1800,1,1))

    def __str__(self):
        return self.user.username


class CompanyProfile(Profile):
    def __init__(self,user):
        super().__init__(user)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
