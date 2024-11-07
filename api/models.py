from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Кастомизация модели пользователя."""
    
    fio = models.CharField(max_length=255, blank=False)
    number_phone = models.CharField(max_length=15, blank=False)
    number_card = models.CharField(max_length=19, blank=False)
    
    def __str__(self):
        return self.fio