# Generated by Django 2.2.6 on 2019-11-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stegnoraphy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='iid',
            field=models.IntegerField(default=0),
        ),
    ]
