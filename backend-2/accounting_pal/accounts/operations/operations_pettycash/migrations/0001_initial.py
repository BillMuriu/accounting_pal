# Generated by Django 5.1 on 2024-12-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PettyCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(default='', max_length=100)),
                ('payee_name', models.CharField(default='', max_length=100)),
                ('cheque_number', models.CharField(default='', max_length=20, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, default='')),
                ('date_issued', models.DateTimeField()),
            ],
        ),
    ]
