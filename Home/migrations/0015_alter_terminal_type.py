# Generated by Django 4.1.3 on 2022-11-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_alter_residence_graid_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal',
            name='type',
            field=models.CharField(choices=[('Bu', 'BUS'), ('Tr', 'TRAIN'), ('Pl', 'AIR_PLAN'), ('Cr', 'CRUISE')], max_length=2),
        ),
    ]
