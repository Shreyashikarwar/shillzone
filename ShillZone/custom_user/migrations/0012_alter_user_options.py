# Generated by Django 3.2.7 on 2021-10-30 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0011_user_created_dt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'User_Info'},
        ),
    ]