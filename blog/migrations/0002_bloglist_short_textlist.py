# Generated by Django 3.0.4 on 2020-05-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloglist',
            name='short_textlist',
            field=models.TextField(blank=True),
        ),
    ]
