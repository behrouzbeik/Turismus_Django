# Generated by Django 4.1.3 on 2022-11-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_residence_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='residence',
            name='graid_star',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
