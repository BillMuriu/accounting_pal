from django.db import models

class OpeningBalance(models.Model):
    account = models.CharField(max_length=100)
    date = models.DateTimeField()
    bank_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cash_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return f"Opening Balance - {self.account} on {self.date}: Bank {self.bank_amount}, Cash {self.cash_amount}"