# Generated by Django 3.2.7 on 2021-10-09 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='comment',
            field=models.TextField(max_length=1000),
        ),
    ]