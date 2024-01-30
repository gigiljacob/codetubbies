# Generated by Django 4.2 on 2024-01-30 09:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='events',
            name='updated_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, default=datetime.datetime(2024, 1, 30, 15, 4, 16, 410955)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participant',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='updated_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, default=datetime.datetime(2024, 1, 30, 15, 4, 20, 277782)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speakers',
            name='created_at',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AddField(
            model_name='speakers',
            name='updated_at',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, default=datetime.datetime(2024, 1, 30, 15, 4, 25, 777893)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speakers',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]