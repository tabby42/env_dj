from django.contrib import admin
from .models import Sunshine

# Register your models here.
#admin.site.register(Sunshine)

@admin.register(Sunshine)
class SunshineAdmin(admin.ModelAdmin):
    list_display = ('date', 'sunbeam_1', 'sunbeam_2', 'sunbeam_3', 'is_completed', 'user')


