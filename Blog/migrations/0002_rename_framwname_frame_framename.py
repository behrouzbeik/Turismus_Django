# Generated by Django 4.1.3 on 2022-11-27 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frame',
            old_name='framwName',
            new_name='frameName',
        ),
    ]
