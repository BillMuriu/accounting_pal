# Generated by Django 5.1 on 2024-12-11 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operations_pettycash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OperationReceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(default='operations_account', max_length=50)),
                ('received_from', models.CharField(max_length=100)),
                ('cash_bank', models.CharField(choices=[('cash', 'Cash'), ('bank', 'Bank')], max_length=4)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rmi_fund', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('other_voteheads', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date', models.DateTimeField()),
                ('petty_cash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='operations_pettycash.pettycash')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
