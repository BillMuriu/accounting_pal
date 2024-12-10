from rest_framework import serializers
from .models import SchoolFundPaymentVoucher

class SchoolFundPaymentVoucherSerializer(serializers.ModelSerializer):
    # Displaying the related OperationReceipt by accessing its fields
    operation_receipt = serializers.SerializerMethodField()

    class Meta:
        model = SchoolFundPaymentVoucher
        fields = ['id', 'voucher_no', 'payee_name', 'particulars', 'amount_shs', 'payment_mode',
                  'total_amount_in_words', 'prepared_by', 'authorised_by', 'vote_head', 'vote_details', 'date', 'operation_receipt']

    # Method to return basic details from the related OperationReceipt
    def get_operation_receipt(self, obj):
        if obj.operation_receipt:
            return {
                'id': obj.operation_receipt.id,
                'account': obj.operation_receipt.account,
                'total_amount': obj.operation_receipt.total_amount,
                'date': obj.operation_receipt.date,
            }
        return None
