from rest_framework import serializers
from .models import OperationReceipt
from accounts.operations.operations_pettycash.models import PettyCash
from accounts.operations.operations_pettycash.serializers import PettyCashSerializer
from accounts.school_fund.school_fund_paymentvouchers.serializers import SchoolFundPaymentVoucherSerializer

class OperationReceiptSerializer(serializers.ModelSerializer):
    receivedFrom = serializers.CharField(source='received_from')
    cashBank = serializers.CharField(source='cash_bank')
    totalAmount = serializers.DecimalField(source='total_amount', max_digits=10, decimal_places=2)
    
    # Allow rmiFund and otherVoteheads to accept null values
    rmiFund = serializers.DecimalField(source='rmi_fund', max_digits=10, decimal_places=2, allow_null=True)
    otherVoteheads = serializers.DecimalField(source='other_voteheads', max_digits=10, decimal_places=2, allow_null=True)
    
    # Use PrimaryKeyRelatedField for input, allowing null values
    petty_cash = serializers.PrimaryKeyRelatedField(queryset=PettyCash.objects.all(), required=False, allow_null=True)

    # Read-only field for the related SchoolFundPaymentVoucher
    school_fund_voucher = SchoolFundPaymentVoucherSerializer(read_only=True)

    class Meta:
        model = OperationReceipt
        fields = ['id', 'account', 'receivedFrom', 'cashBank', 'totalAmount', 'rmiFund', 'otherVoteheads', 'date', 'petty_cash', 'school_fund_voucher']

    # Add this method to include related PettyCash and SchoolFundPaymentVoucher details on read operations
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Include the petty cash details when viewing the receipt
        if instance.petty_cash:
            representation['petty_cash'] = PettyCashSerializer(instance.petty_cash).data
        
        # Include the school fund payment voucher details if linked
        if hasattr(instance, 'school_fund_voucher'):
            representation['school_fund_voucher'] = SchoolFundPaymentVoucherSerializer(instance.school_fund_voucher).data
        
        return representation
