# Generated by Django 4.1.3 on 2022-12-03 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_specialposition'),
        ('Home', '0017_remove_transport_stars_transport_graid_star_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='detail_article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.article'),
        ),
    ]