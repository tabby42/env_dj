# Generated by Django 4.0.2 on 2022-02-04 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apenv_dj', '0002_sunny_day_sunny_day_url_sunny_day_is_completed_sunny_day_is_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='sunny_day',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
