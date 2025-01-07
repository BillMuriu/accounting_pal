from django.db import models
from accounts.operations.operations_receipts.models import OperationReceipt  # Import the OperationReceipt model
from accounts.rmi.rmi_receipts.models import RMIReceipt
from accounts.tuition.tuition_receipts.models import TuitionReceipt  # Import TuitionReceipt model

class SchoolFundPaymentVoucher(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('cash', 'Cash'),
        ('bank', 'Bank'),
    ]

    VOTE_HEAD_CHOICES = [
        ('rmi', 'RMI'),
        ('operations', 'Operations'),
        ('tuition', 'Tuition'),
        ('other_voteheads', 'Other Voteheads'),
    ]

    account = models.CharField(max_length=255, default='school_fund_account')
    voucher_no = models.PositiveIntegerField()
    payee_name = models.CharField(max_length=255)
    particulars = models.TextField()
    amount_shs = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES)
    total_amount_in_words = models.CharField(max_length=255)
    prepared_by = models.CharField(max_length=255)
    authorised_by = models.CharField(max_length=255)
    vote_head = models.CharField(max_length=50, choices=VOTE_HEAD_CHOICES)  # Adding vote_head with choices
    vote_details = models.TextField()
    date = models.DateTimeField()

    # Adding cheque_number field
    cheque_number = models.CharField(max_length=255, blank=True, null=True, help_text="Cheque number, if applicable")

    # One-to-One relationship with RMIPaymentVoucher
    rmi_receipt = models.OneToOneField(
        RMIReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='school_fund_payment_voucher'
    )

    # One-to-One relationship with OperationReceipt
    operation_receipt = models.OneToOneField(
        OperationReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='school_fund_voucher'
    )

    # One-to-One relationship with TuitionReceipt
    tuition_receipt = models.OneToOneField(
        TuitionReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='school_fund_voucher'
    )

    def __str__(self):
        return f"School Fund Payment Voucher #{self.voucher_no} - {self.payee_name}"
