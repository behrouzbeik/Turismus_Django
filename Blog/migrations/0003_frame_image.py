# Generated by Django 4.1.3 on 2022-11-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_rename_framwname_frame_framename'),
    ]

    operations = [
        migrations.AddField(
            model_name='frame',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]