# Generated by Django 3.2.7 on 2021-10-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_createnewpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='createnewpage',
            options={'verbose_name_plural': 'Coin Page'},
        ),
        migrations.AlterField(
            model_name='adduser',
            name='created_dt',
            field=models.DateTimeField(auto_now=True, db_column='Created Date'),
        ),
        migrations.AlterField(
            model_name='createnewpage',
            name='created_dt',
            field=models.DateTimeField(auto_now=True, db_column='Created Date'),
        ),
        migrations.AlterModelTable(
            name='createnewpage',
            table='coin_page',
        ),
    ]