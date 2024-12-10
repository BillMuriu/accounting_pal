from django.db import models
from accounts.tuition.tuition_pettycash.models import TuitionPettyCash

class TuitionReceipt(models.Model):
    TUITION_ACCOUNT = 'tuition_account'
    
    CASH_BANK_CHOICES = [
        ('cash', 'Cash'),
        ('bank', 'Bank'),
    ]
    
    ACCOUNT_CHOICES = [
        (TUITION_ACCOUNT, 'Tuition Account'),
    ]

    account = models.CharField(max_length=50, choices=ACCOUNT_CHOICES, default=TUITION_ACCOUNT)
    received_from = models.CharField(max_length=100, help_text="Name of the payer (could be a student or another entity)")
    cash_bank = models.CharField(max_length=4, choices=CASH_BANK_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total amount received")
    date = models.DateTimeField(help_text="Date of receipt")
    petty_cash = models.OneToOneField(TuitionPettyCash, on_delete=models.SET_NULL, null=True, blank=True, related_name='tuition_receipt', help_text="Associated petty cash, if any")

    def __str__(self):
        return f"Receipt from {self.received_from} on {self.date} (Total: {self.total_amount})"

    class Meta:
        ordering = ['-date']
