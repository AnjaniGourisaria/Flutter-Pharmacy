# Generated by Django 4.0.2 on 2022-02-27 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apisetup', '0002_consumer_contacts_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='otp',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='address',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='browser',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='city',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='email',
            field=models.EmailField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='local_ip',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='mac_address',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='router_ip',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='state',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='station',
            field=models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Work', 'Works'), ('Others', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='publish_date'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='zipcode',
            field=models.IntegerField(default='', null=True),
        ),
    ]