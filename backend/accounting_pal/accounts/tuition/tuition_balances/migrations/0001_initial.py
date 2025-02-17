# Generated by Django 4.1.7 on 2024-10-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TuitionOpeningBalance',
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
