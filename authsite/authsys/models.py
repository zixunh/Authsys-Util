import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.CharField(verbose_name='user_id', primary_key=True, max_length = 50, default=uuid.uuid4, editable=False, auto_created=True)
    name = models.CharField(blank=True, max_length=255)
    def __str__(self):
        return self.email
