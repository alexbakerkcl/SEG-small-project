# Generated by Django 3.2.5 on 2021-12-17 14:48

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_auto_20211217_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.CharField(choices=[('N', 'New to Chess'), ('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced'), ('E', 'Expert')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
