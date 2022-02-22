from datetime import datetime
from statistics import mode
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models

# Create your models here.


class Data(models.Model):
    name = models.CharField("نام نام خانوادگی و ", max_length=100)
    title = models.CharField("عنوان ", max_length=100)
    phone_number = models.CharField(" شماره تماس ", max_length=100)
    create_at = models.FloatField(default=datetime.now().timestamp())
    city = models.CharField(" شهر اقامت", max_length=100)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name:"کاربر"
        verbose_name_plural = "کاربران"