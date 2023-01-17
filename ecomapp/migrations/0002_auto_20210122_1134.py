# Generated by Django 3.0.6 on 2021-01-22 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amountpaid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='oid',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='orders',
            name='paymentstatus',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
