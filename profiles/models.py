from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_support = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} is support' if self.is_support else self.user.username

    class Meta:
        ordering = ('id',)
