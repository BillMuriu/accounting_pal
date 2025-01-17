from rest_framework import serializers
from .models import SchoolFundPaymentVoucher


class SchoolFundPaymentVoucherSerializer(serializers.ModelSerializer):
    # Display related OperationReceipt, RMIReceipt, and TuitionReceipt details
    operation_receipt = serializers.SerializerMethodField()
    rmi_receipt = serializers.SerializerMethodField()
    tuition_receipt = serializers.SerializerMethodField()

    class Meta:
        model = SchoolFundPaymentVoucher
        fields = [
            'id', 'account','voucher_no', 'payee_name', 'particulars', 'amount_shs', 'payment_mode',
            'total_amount_in_words', 'prepared_by', 'authorised_by', 'vote_head', 'vote_details',
            'date', 'operation_receipt', 'rmi_receipt', 'tuition_receipt'
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

    # Method to return basic details from the related RMIReceipt
    def get_rmi_receipt(self, obj):
        if obj.rmi_receipt:
            return {
                'id': obj.rmi_receipt.id,
                'account': obj.rmi_receipt.account,
                'total_amount': obj.rmi_receipt.total_amount,
                'date': obj.rmi_receipt.date,
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
