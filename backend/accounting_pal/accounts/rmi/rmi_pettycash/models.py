from django.db import models

class RMIPettyCash(models.Model):
    account = models.CharField(max_length=100, default='rmi_account')  # Specific account type
    payee_name = models.CharField(max_length=100, default='')
    cheque_number = models.CharField(max_length=20, unique=True, default='')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, default='')  # Optional description field
    date_issued = models.DateTimeField()

    def __str__(self):
        return f"RMI Petty Cash - {self.amount} ({self.date_issued}) - Payee: {self.payee_name}"
