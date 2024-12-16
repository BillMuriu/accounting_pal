# Generated by Django 4.1.7 on 2024-12-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TuitionBankCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('charge_date', models.DateTimeField()),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
    ]
