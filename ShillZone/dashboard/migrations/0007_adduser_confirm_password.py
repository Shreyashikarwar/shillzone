# Generated by Django 3.2.7 on 2021-10-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20211020_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='adduser',
            name='confirm_password',
            field=models.TextField(db_column='confirm password', max_length=100, null=True),
        ),
    ]