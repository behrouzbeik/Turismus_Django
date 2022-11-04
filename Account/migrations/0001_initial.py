# Generated by Django 4.1.3 on 2022-11-02 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=50)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('sheba', models.CharField(blank=True, max_length=50, null=True)),
                ('cardnumber', models.CharField(blank=True, max_length=50, null=True)),
                ('depositnumber', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('usertype', models.CharField(choices=[('Ma', 'MASTER'), ('Tr', 'TRAVELER'), ('Us', 'USER')], max_length=2)),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('unicid', models.CharField(max_length=10)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
                ('gender', models.BooleanField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Walet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.PositiveIntegerField(blank=True, null=True)),
                ('harvest', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField()),
                ('amount', models.PositiveIntegerField()),
                ('cash', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userscore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('residence', models.ManyToManyField(blank=True, null=True, related_name='residence_scr', to='Home.residence')),
                ('room', models.ManyToManyField(blank=True, null=True, related_name='room_scr', to='Home.room')),
                ('tour', models.ManyToManyField(blank=True, null=True, related_name='tour_scr', to='Home.tour')),
                ('transport', models.ManyToManyField(blank=True, null=True, related_name='transport_scr', to='Home.transport')),
                ('transportcompany', models.ManyToManyField(blank=True, null=True, related_name='transportco_scr', to='Home.transportco')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.PositiveIntegerField(blank=True, null=True)),
                ('hervest', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField()),
                ('amount', models.PositiveIntegerField()),
                ('cash', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]