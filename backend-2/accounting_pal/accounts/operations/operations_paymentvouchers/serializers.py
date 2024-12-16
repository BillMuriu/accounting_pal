from rest_framework import serializers
from .models import PaymentVoucher

class PaymentVoucherSerializer(serializers.ModelSerializer):
    voucherNo = serializers.IntegerField(source='voucher_no')
    payeeName = serializers.CharField(source='payee_name')
    amountShs = serializers.DecimalField(source='amount_shs', max_digits=10, decimal_places=2)
    paymentMode = serializers.CharField(source='payment_mode')
    totalAmountInWords = serializers.CharField(source='total_amount_in_words')
    preparedBy = serializers.CharField(source='prepared_by')
    authorisedBy = serializers.CharField(source='authorised_by')
    voteHead = serializers.CharField(source='vote_head')
    voteDetails = serializers.CharField(source='vote_details')
    date = serializers.DateTimeField()

    # Custom method to include related receipts
    schoolFundReceipt = serializers.SerializerMethodField()
    rmiReceipt = serializers.SerializerMethodField()

    class Meta:
        model = PaymentVoucher
        fields = [
            'id', 'account', 'voucherNo', 'payeeName', 'particulars', 
            'amountShs', 'paymentMode', 'totalAmountInWords', 'preparedBy', 
            'authorisedBy', 'voteHead', 'voteDetails', 'date', 
            'schoolFundReceipt', 'rmiReceipt'  # Include both receipt fields
        ]

    def get_schoolFundReceipt(self, obj):
        if hasattr(obj, 'school_fund_receipt') and obj.school_fund_receipt is not None:
            receipt = obj.school_fund_receipt
            return {
                'id': receipt.id,
                'received_from': receipt.received_from,
                'date': receipt.date,
                'total_amount': receipt.total_amount,
            }
        return None

    def get_rmiReceipt(self, obj):
        if hasattr(obj, 'rmi_receipt') and obj.rmi_receipt is not None:
            receipt = obj.rmi_receipt
            return {
                'id': receipt.id,
                'received_from': receipt.received_from,
                'date': receipt.date,
                'total_amount': receipt.total_amount,
            }
        return None
