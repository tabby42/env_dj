from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sunshine (models.Model):
    date = models.DateField()
    sunbeam_1 = models.TextField(max_length=250, verbose_name='Sunbeam #1', null=True, blank=True)
    sunbeam_2 = models.TextField(max_length=250, verbose_name='Sunbeam #2', null=True, blank=True)
    sunbeam_3 = models.TextField(max_length=250, verbose_name='Sunbeam #3', null=True, blank=True)
    is_completed = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

