# Generated by Django 5.1 on 2024-12-31 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations_paymentvouchers', '0002_paymentvoucher_tuition_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentvoucher',
            name='cheque_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
