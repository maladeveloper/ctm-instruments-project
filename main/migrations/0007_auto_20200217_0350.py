# Generated by Django 3.0.3 on 2020-02-17 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200216_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='instrument_image',
        ),
        migrations.AddField(
            model_name='instrument',
            name='image_url',
            field=models.TextField(default='image.png'),
        ),
    ]
