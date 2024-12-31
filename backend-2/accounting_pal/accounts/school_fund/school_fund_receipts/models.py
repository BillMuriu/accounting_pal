from django.db import models
from students.students.models import Student
from accounts.school_fund.school_fund_pettycash.models import SchoolFundPettyCash


class SchoolFundReceipt(models.Model):
    SCHOOL_FUND_ACCOUNT = 'school_fund_account'
    
    CASH_BANK_CHOICES = [
        ('cash', 'Cash'),
        ('bank', 'Bank'),
    ]
    
    ACCOUNT_CHOICES = [
        (SCHOOL_FUND_ACCOUNT, 'School Fund Account'),
    ]

    account = models.CharField(max_length=50, choices=ACCOUNT_CHOICES, default=SCHOOL_FUND_ACCOUNT)
    received_from = models.CharField(max_length=100, help_text="Name of the payer (could be a student or another entity)")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, help_text="The student associated with this receipt, if applicable")
    cash_bank = models.CharField(max_length=4, choices=CASH_BANK_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Total amount received")
    date = models.DateTimeField(help_text="Date of receipt")
    petty_cash = models.OneToOneField(SchoolFundPettyCash, on_delete=models.SET_NULL, null=True, blank=True, related_name='school_fund_receipt', help_text="Associated petty cash, if any")
    receipt_number = models.CharField(max_length=50, null=True, blank=True, help_text="Optional receipt number for this transaction")

    def __str__(self):
        return f"Receipt from {self.received_from} on {self.date} (Total: {self.total_amount})"

    class Meta:
        ordering = ['-date']
