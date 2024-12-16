from rest_framework import serializers
from .models import RMIPaymentVoucher

class RMIPaymentVoucherSerializer(serializers.ModelSerializer):
    # Displaying the related OperationReceipt, SchoolFundReceipt, and TuitionReceipt by accessing their fields
    operation_receipt = serializers.SerializerMethodField()
    school_fund_receipt = serializers.SerializerMethodField()
    tuition_receipt = serializers.SerializerMethodField()

    class Meta:
        model = RMIPaymentVoucher
        fields = [
            'id',
            'account',
            'voucher_no', 
            'payee_name', 
            'particulars', 
            'amount_shs',
            'payment_mode', 
            'total_amount_in_words',  
            'prepared_by', 
            'authorised_by',
            'vote_head',  
            'vote_details',
            'date',
            'operation_receipt',
            'school_fund_receipt',
            'tuition_receipt'
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

    # Method to return basic details from the related TuitionReceipt
    def get_tuition_receipt(self, obj):
        if obj.tuition_receipt:
            return {
                'id': obj.tuition_receipt.id,
                'account': obj.tuition_receipt.account,
                'total_amount': obj.tuition_receipt.total_amount,
                'date': obj.tuition_receipt.date,
            }
        return None
