# Generated by Django 4.1.2 on 2022-11-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_mycompanyinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycompanyinfo',
            name='company_name',
            field=models.CharField(default='#', max_length=50),
        ),
    ]
