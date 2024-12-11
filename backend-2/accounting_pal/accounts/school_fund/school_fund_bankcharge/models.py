from django.db import models

class SchoolFundBankCharges(models.Model):
    account = models.CharField(max_length=255, default='school_fund_account')  # School fund specific account
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # For the charge amount
    charge_date = models.DateTimeField()  # Date and time of the charge
    description = models.TextField(blank=True, default='')  # Optional description of the charge

    def __str__(self):
        return f"School Fund Bank Charge - {self.amount} on {self.charge_date} ({self.account})"
