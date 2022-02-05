from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings 

# Create your models here.
class Sunshine (models.Model):
    date = models.DateField(default=datetime.date.today)
    sunbeam_1 = models.TextField(max_length=150, verbose_name='Good Thing #1', null=True, blank=True)
    sunbeam_2 = models.TextField(max_length=150, verbose_name='Good Thing #2', null=True, blank=True)
    sunbeam_3 = models.TextField(max_length=150, verbose_name='Good Thing #3', null=True, blank=True)
    is_completed = models.BooleanField(default = False, verbose_name='Completed')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}, {}, {}'.format(self.sunbeam_1, self.sunbeam_2, self.sunbeam_3)
    class Meta:
        ordering = ['-date']

