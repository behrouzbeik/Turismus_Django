# Generated by Django 4.1.3 on 2022-11-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_residence_buyscore_alter_residence_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residence',
            name='graid_star',
            field=models.PositiveBigIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=0, null=True),
        ),
    ]