# Generated by Django 3.2.7 on 2021-10-01 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]