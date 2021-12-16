# Generated by Django 3.2.5 on 2021-12-16 06:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='followees', to=settings.AUTH_USER_MODEL),
        ),
    ]
