# Generated by Django 4.1.7 on 2024-10-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition_paymentvouchers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuitionpaymentvoucher',
            name='cheque_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
