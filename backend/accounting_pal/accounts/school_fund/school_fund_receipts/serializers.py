from rest_framework import serializers
from .models import SchoolFundReceipt
from accounts.operations.operations_paymentvouchers.serializers import PaymentVoucherSerializer

class SchoolFundReceiptSerializer(serializers.ModelSerializer):
    # Nested serializer to show the related PaymentVoucher
    paymentVoucher = PaymentVoucherSerializer(source='payment_voucher', read_only=True)

    class Meta:
        model = SchoolFundReceipt
        fields = [
            'id', 'account', 'received_from', 'student', 
            'cash_bank', 'total_amount', 'date', 'paymentVoucher'
        ]
