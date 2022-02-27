# Generated by Django 4.0.2 on 2022-02-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apisetup', '0004_alter_consumer_address_alter_consumer_browser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='address',
            field=models.CharField(default='0', max_length=500),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='city',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='email',
            field=models.EmailField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='state',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='station',
            field=models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Work', 'Works'), ('Others', 'Others')], default='Home', max_length=20),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='zipcode',
            field=models.IntegerField(default='0'),
        ),
    ]