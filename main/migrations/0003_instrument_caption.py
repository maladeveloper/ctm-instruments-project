# Generated by Django 3.0.3 on 2020-02-09 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_instrument_instrument_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='caption',
            field=models.TextField(default='a string instrument'),
            preserve_default=False,
        ),
    ]