# Generated by Django 4.1.7 on 2024-12-16 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rmi_receipts', '0001_initial'),
        ('school_fund_receipts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(default='operations_account', max_length=255)),
                ('voucher_no', models.PositiveIntegerField()),
                ('payee_name', models.CharField(max_length=255)),
                ('particulars', models.TextField()),
                ('amount_shs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_mode', models.CharField(choices=[('cash', 'Cash'), ('bank', 'Bank')], max_length=50)),
                ('total_amount_in_words', models.CharField(max_length=255)),
                ('prepared_by', models.CharField(max_length=255)),
                ('authorised_by', models.CharField(max_length=255)),
                ('vote_head', models.CharField(choices=[('rmi', 'RMI'), ('school_fund', 'School Fund'), ('tuition', 'Tuition'), ('other_voteheads', 'Other Voteheads')], max_length=50)),
                ('vote_details', models.TextField()),
                ('date', models.DateTimeField()),
                ('rmi_receipt', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_voucher', to='rmi_receipts.rmireceipt')),
                ('school_fund_receipt', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_voucher', to='school_fund_receipts.schoolfundreceipt')),
            ],
        ),
    ]
