# Generated by Django 5.1 on 2024-12-16 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition_paymentvouchers', '0002_tuitionpaymentvoucher_rmi_receipt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuitionpaymentvoucher',
            name='vote_head',
            field=models.CharField(choices=[('school_fund', 'School fund'), ('operations', 'Operations'), ('rmi', 'rmi'), ('other_voteheads', 'Other Voteheads')], max_length=50),
        ),
    ]
