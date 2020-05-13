# Generated by Django 3.0.4 on 2020-05-13 12:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carmanager', '0003_carmanager_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_list', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('name_list', models.CharField(max_length=300)),
                ('blog_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('text_list', models.TextField(blank=True)),
                ('visible_list', models.BooleanField(blank=True)),
                ('rating', models.IntegerField(default=True)),
                ('carmanager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carmanager.CarManager')),
            ],
        ),
    ]
