from django.db import models
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt
from accounts.operations.operations_receipts.models import OperationReceipt
from accounts.tuition.tuition_receipts.models import TuitionReceipt  # Import TuitionReceipt

class RMIPaymentVoucher(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('cash', 'Cash'),
        ('bank', 'Bank'),
    ]

    VOTE_HEAD_CHOICES = [
        ('school_fund', 'School fund'),
        ('operations', 'Operations'),
        ('tuition', 'Tuition'),
        ('other_voteheads', 'Other Voteheads'),
    ]

    account = models.CharField(max_length=255, default='rmi_account')
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

    # One-to-One relationship with OperationReceipt
    operation_receipt = models.OneToOneField(
        OperationReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rmi_payment_voucher'
    )

    # One-to-One relationship with SchoolFundReceipt
    school_fund_receipt = models.OneToOneField(
        SchoolFundReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rmi_payment_voucher'
    )

    # One-to-One relationship with TuitionReceipt
    tuition_receipt = models.OneToOneField(
        TuitionReceipt,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rmi_payment_voucher'
    )

    def __str__(self):
        return f"RMI Payment Voucher #{self.voucher_no} - {self.payee_name}"
