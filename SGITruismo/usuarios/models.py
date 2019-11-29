from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # add additional fields in here
    empresa_id = models.IntegerField(null=True)
    def __str__(self):
        return self.username
