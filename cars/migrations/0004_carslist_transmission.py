# Generated by Django 3.0.4 on 2020-04-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200401_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='carslist',
            name='transmission',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]