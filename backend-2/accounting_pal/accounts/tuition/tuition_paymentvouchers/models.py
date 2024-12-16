from django.db import models
from accounts.operations.operations_receipts.models import OperationReceipt
from accounts.rmi.rmi_receipts.models import RMIReceipt  # Import RMIReceipt
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt  # Import SchoolFundReceipt

class TuitionPaymentVoucher(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('cash', 'Cash'),
        ('bank', 'Bank'),
    ]

    VOTE_HEAD_CHOICES = [
        ('school_fund', 'School fund'),
        ('operations', 'Operations'),
        ('rmi', 'rmi'),
        ('other_voteheads', 'Other Voteheads'),
    ]

    account = models.CharField(max_length=255, default='tuition_account')  # Set to tuition account
    voucher_no = models.PositiveIntegerField()
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

    # Optional cheque number field
    cheque_number = models.CharField(max_length=255, null=True, blank=True)

    # One-to-One relationship with OperationReceipt
    operation_receipt = models.OneToOneField(
        OperationReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tuition_payment_voucher'  # Updated related name
    )

    # One-to-One relationship with RMIReceipt
    rmi_receipt = models.OneToOneField(
        RMIReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tuition_payment_voucher'
    )

    # One-to-One relationship with SchoolFundReceipt
    school_fund_receipt = models.OneToOneField(
        SchoolFundReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tuition_payment_voucher'
    )

    def __str__(self):
        return f"Tuition Payment Voucher #{self.voucher_no} - {self.payee_name}"
