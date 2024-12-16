from django.db import models
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt
from accounts.rmi.rmi_receipts.models import RMIReceipt
from django.contrib import auth

class PaymentVoucher(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('cash', 'Cash'),
        ('bank', 'Bank'),
    ]

    VOTE_HEAD_CHOICES = [
        ('rmi', 'RMI'),
        ('school_fund', 'School Fund'),
        ('tuition', 'Tuition'),
        ('other_voteheads', 'Other Voteheads'),
    ]

    account = models.CharField(max_length=255, default='operations_account')

    voucher_no = models.PositiveIntegerField()  # Voucher number as a numeric field
    payee_name = models.CharField(max_length=255)
    particulars = models.TextField()
    amount_shs = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES)
    total_amount_in_words = models.CharField(max_length=255)
    prepared_by = models.CharField(max_length=255)
    authorised_by = models.CharField(max_length=255)
    vote_head = models.CharField(max_length=50, choices=VOTE_HEAD_CHOICES)
    vote_details = models.TextField()
    date = models.DateTimeField()

    # Relationships to Receipts
    school_fund_receipt = models.OneToOneField(
        SchoolFundReceipt,
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='payment_voucher'
    )

    rmi_receipt = models.OneToOneField(  # Add relationship for RMI Receipt
        RMIReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='payment_voucher'
    )

    def __str__(self):
        return f"Payment Voucher #{self.voucher_no} - {self.payee_name}"
