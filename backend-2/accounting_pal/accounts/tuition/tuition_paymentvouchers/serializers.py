from rest_framework import serializers
from .models import TuitionPaymentVoucher

class TuitionPaymentVoucherSerializer(serializers.ModelSerializer):
    # Displaying the related OperationReceipt by accessing its fields
    operation_receipt = serializers.SerializerMethodField()
    school_fund_receipt = serializers.SerializerMethodField()
    rmi_receipt = serializers.SerializerMethodField()

    class Meta:
        model = TuitionPaymentVoucher
        fields = [
            'id', 'account', 'voucher_no', 'payee_name', 'particulars', 
            'amount_shs', 'payment_mode', 'total_amount_in_words', 
            'prepared_by', 'authorised_by', 'vote_head', 
            'vote_details', 'date', 'cheque_number', 
            'operation_receipt', 'school_fund_receipt', 'rmi_receipt'
        ]

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

    # Method to return basic details from the related SchoolFundReceipt
    def get_school_fund_receipt(self, obj):
        if obj.school_fund_receipt:
            return {
                'id': obj.school_fund_receipt.id,
                'account': obj.school_fund_receipt.account,
                'total_amount': obj.school_fund_receipt.total_amount,
                'date': obj.school_fund_receipt.date,
            }
        return None

    # Method to return basic details from the related RMIFundReceipt
    def get_rmi_receipt(self, obj):
        if obj.rmi_receipt:
            return {
                'id': obj.rmi_receipt.id,
                'account': obj.rmi_receipt.account,
                'total_amount': obj.rmi_receipt.total_amount,
                'date': obj.rmi_receipt.date,
            }
        return None
