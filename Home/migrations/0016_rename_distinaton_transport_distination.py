# Generated by Django 4.1.3 on 2022-11-12 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0015_alter_terminal_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transport',
            old_name='distinaton',
            new_name='distination',
        ),
    ]
