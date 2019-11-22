from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # add additional fields in here
    empleado_id = models.IntegerField()
    def __str__(self):
        return self.username
