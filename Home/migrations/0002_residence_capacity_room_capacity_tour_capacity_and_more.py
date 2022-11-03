# Generated by Django 4.1.3 on 2022-11-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='residence',
            name='capacity',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='capacity',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transport',
            name='capacity',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
