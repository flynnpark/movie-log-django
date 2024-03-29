from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    GENDER_CHOICE = (
        ('male', 'Male'),
        ('femail', 'Female'),
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null=True, blank=True)
    name = models.CharField(_('Name of User'), max_length=255)
    gender = models.CharField(max_length=32, choices=GENDER_CHOICE, null=True)
    phone = models.CharField(max_length=32, null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
