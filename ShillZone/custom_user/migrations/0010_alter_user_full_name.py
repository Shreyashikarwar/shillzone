# Generated by Django 3.2.7 on 2021-10-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0009_rename_fullname_user_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, db_column='full_name', max_length=250, null=True),
        ),
    ]