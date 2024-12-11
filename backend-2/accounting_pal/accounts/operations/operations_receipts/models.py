from django.db import models
from accounts.operations.operations_pettycash.models import PettyCash

class OperationReceipt(models.Model):
    OPERATIONS_ACCOUNT = 'operations_account'
    
    CASH_BANK_CHOICES = [
        ('cash', 'Cash'),
        ('bank', 'Bank'),
    ]
    
    account = models.CharField(max_length=50, default=OPERATIONS_ACCOUNT)
    received_from = models.CharField(max_length=100)
    cash_bank = models.CharField(max_length=4, choices=CASH_BANK_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    rmi_fund = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_voteheads = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    date = models.DateTimeField()
    petty_cash = models.ForeignKey(PettyCash, on_delete=models.CASCADE, null=True, blank=True, related_name='receipts')

    def __str__(self):
        return f"Receipt from {self.received_from} on {self.date}"

    class Meta:
        ordering = ['-date']
