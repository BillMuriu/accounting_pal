from django.db import models

class BankCharges(models.Model):
    account = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    charge_date = models.DateTimeField()
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return f"Bank Charge - {self.amount} on {self.charge_date} ({self.account})"
