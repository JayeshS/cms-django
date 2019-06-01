from django.db import models
from django.conf import settings
from .site import Site
from .organization import Organization


class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    regions = models.ManyToManyField(Site, blank=True)
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

    class Meta():
        permissions = (
            ('view_user_profile', 'Can view user profile'),
        )