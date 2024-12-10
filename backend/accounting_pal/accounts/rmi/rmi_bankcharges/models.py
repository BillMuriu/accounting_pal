from django.db import models

class RMIBankCharge(models.Model):
    account = models.CharField(max_length=255)  # The account associated with the bank charge
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # The amount of the charge
    charge_date = models.DateTimeField()  # The date of the charge
    description = models.TextField(blank=True, default='')  # Optional description for the charge

    def __str__(self):
        return f"RMI Bank Charge - {self.amount} on {self.charge_date} ({self.account})"
