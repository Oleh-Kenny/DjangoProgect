# Generated by Django 3.0.4 on 2020-04-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmanager', '0002_auto_20200405_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmanager',
            name='rating',
            field=models.IntegerField(default=True),
        ),
    ]
