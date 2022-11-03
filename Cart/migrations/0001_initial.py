# Generated by Django 4.1.3 on 2022-11-03 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0002_residence_capacity_room_capacity_tour_capacity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.CharField(max_length=10, unique=True)),
                ('ordertime', models.DateTimeField(auto_now_add=True)),
                ('adult', models.PositiveIntegerField()),
                ('child', models.PositiveIntegerField(blank=True, null=True)),
                ('baby', models.PositiveIntegerField(blank=True, null=True)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.room')),
                ('tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.tour')),
                ('transport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.transport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RefundRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refundtime', models.DateTimeField(auto_now_add=True)),
                ('refundprice', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Pe', 'PENDING'), ('Re', 'READY'), ('Pa', 'PAID')], max_length=2)),
                ('Order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Un', 'UNPAID'), ('Pa', 'PAID'), ('Ca', 'CANCEL'), ('Do', 'DONE')], max_length=2)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.order')),
            ],
        ),
        migrations.CreateModel(
            name='Order_User_Rel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ManyToManyField(related_name='order_rel', to='Cart.order')),
                ('traveler', models.ManyToManyField(related_name='user_rel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.PositiveIntegerField()),
                ('child', models.PositiveIntegerField(blank=True, null=True)),
                ('baby', models.PositiveIntegerField(blank=True, null=True)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.room')),
                ('tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.tour')),
                ('transport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.transport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
