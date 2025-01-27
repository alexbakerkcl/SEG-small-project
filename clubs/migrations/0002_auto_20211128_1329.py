# Generated by Django 3.2.5 on 2021-11-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.CharField(choices=[('N', 'New to Chess'), ('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced'), ('E', 'Expert')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='statement',
            field=models.TextField(blank=True, max_length=520),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=520),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
