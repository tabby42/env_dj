from django.contrib import admin
from .models import Goal

# Register your models here.
#admin.site.register(Goal)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_started', 'is_completed')


