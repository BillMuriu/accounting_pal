# Generated by Django 5.1 on 2024-12-16 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmi_receipts', '0001_initial'),
        ('school_fund_receipts', '0001_initial'),
        ('tuition_paymentvouchers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuitionpaymentvoucher',
            name='rmi_receipt',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tuition_payment_voucher', to='rmi_receipts.rmireceipt'),
        ),
        migrations.AddField(
            model_name='tuitionpaymentvoucher',
            name='school_fund_receipt',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tuition_payment_voucher', to='school_fund_receipts.schoolfundreceipt'),
        ),
    ]
