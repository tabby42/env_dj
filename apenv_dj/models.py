from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Goal (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    goal_url = models.URLField(blank=True)
    is_started = models.BooleanField(default = False)
    is_completed = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

