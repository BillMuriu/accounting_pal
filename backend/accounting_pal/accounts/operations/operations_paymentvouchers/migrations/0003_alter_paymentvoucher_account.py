# Generated by Django 5.1 on 2024-08-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations_paymentvouchers', '0002_paymentvoucher_account_alter_paymentvoucher_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentvoucher',
            name='account',
            field=models.CharField(default='operations_account', max_length=255),
        ),
    ]
