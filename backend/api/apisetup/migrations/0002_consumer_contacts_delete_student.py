# Generated by Django 4.0.2 on 2022-02-27 16:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apisetup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(default='')),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('zipcode', models.IntegerField(default='')),
                ('station', models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Work', 'Works'), ('Others', 'Others')], max_length=20)),
                ('address', models.CharField(default='', max_length=500)),
                ('email', models.EmailField(default='', max_length=100)),
                ('local_ip', models.CharField(default='', max_length=200)),
                ('browser', models.CharField(default='', max_length=200)),
                ('router_ip', models.CharField(default='', max_length=200)),
                ('mac_address', models.CharField(default='', max_length=100)),
                ('publish_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='publish_date')),
                ('is_deleted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(default='', max_length=30)),
                ('phone', models.IntegerField(default='')),
                ('msg', models.CharField(default='', max_length=900)),
                ('publish_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='publish_date')),
                ('is_deleted', models.BooleanField(default=False)),
                ('reslove', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]