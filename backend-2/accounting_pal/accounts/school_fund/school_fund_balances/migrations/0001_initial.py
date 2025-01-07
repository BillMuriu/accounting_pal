# Generated by Django 5.1 on 2025-01-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolFundOpeningBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('bank_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cash_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
    ]
