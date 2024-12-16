from rest_framework import generics
from .models import RMIPaymentVoucher
from .serializers import RMIPaymentVoucherSerializer
from accounts.operations.operations_receipts.serializers import OperationReceiptSerializer
from accounts.school_fund.school_fund_receipts.serializers import SchoolFundReceiptSerializer
from accounts.tuition.tuition_receipts.serializers import TuitionReceiptSerializer


class ListCreateRMIPaymentVoucherView(generics.ListCreateAPIView):
    queryset = RMIPaymentVoucher.objects.all()
    serializer_class = RMIPaymentVoucherSerializer

    def perform_create(self, serializer):
        rmi_payment_voucher = serializer.save()

        # If the vote head is 'operations', create a corresponding OperationReceipt
        if rmi_payment_voucher.vote_head == 'operations':
            receipt_data = {
                'account': 'operations_account',
                'received_from': rmi_payment_voucher.account,
                'cash_bank': rmi_payment_voucher.payment_mode,
                'total_amount': rmi_payment_voucher.amount_shs,
                'date': rmi_payment_voucher.date,
            }
            receipt_serializer = OperationReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                rmi_payment_voucher.operation_receipt = receipt
                rmi_payment_voucher.save()

        # If the vote head is 'school_fund', create a corresponding SchoolFundReceipt
        elif rmi_payment_voucher.vote_head == 'school_fund':
            receipt_data = {
                'account': 'school_fund_account',
                'received_from': rmi_payment_voucher.account,
                'cash_bank': rmi_payment_voucher.payment_mode,
                'total_amount': rmi_payment_voucher.amount_shs,
                'date': rmi_payment_voucher.date,
            }
            receipt_serializer = SchoolFundReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                rmi_payment_voucher.school_fund_receipt = receipt
                rmi_payment_voucher.save()

        # If the vote head is 'tuition', create a corresponding TuitionReceipt
        elif rmi_payment_voucher.vote_head == 'tuition':
            receipt_data = {
                'account': 'tuition_account',
                'received_from': rmi_payment_voucher.account,
                'cash_bank': rmi_payment_voucher.payment_mode,
                'total_amount': rmi_payment_voucher.amount_shs,
                'date': rmi_payment_voucher.date,
            }
            receipt_serializer = TuitionReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                rmi_payment_voucher.tuition_receipt = receipt
                rmi_payment_voucher.save()

class RMIPaymentVoucherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RMIPaymentVoucher.objects.all()
    serializer_class = RMIPaymentVoucherSerializer

    def perform_update(self, serializer):
        rmi_payment_voucher = serializer.save()

        # Update OperationReceipt if linked
        if rmi_payment_voucher.vote_head == 'operations' and rmi_payment_voucher.operation_receipt:
            receipt_data = {
                'account': 'operations_account',
                'received_from': rmi_payment_voucher.account,
                'cash_bank': rmi_payment_voucher.payment_mode,
                'total_amount': rmi_payment_voucher.amount_shs,
                'date': rmi_payment_voucher.date,
            }
            receipt_serializer = OperationReceiptSerializer(
                rmi_payment_voucher.operation_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

        # Update SchoolFundReceipt if linked
        elif rmi_payment_voucher.vote_head == 'school_fund' and rmi_payment_voucher.school_fund_receipt:
            receipt_data = {
                'account': 'school_fund_account',
                'received_from': rmi_payment_voucher.account,
                'cash_bank': rmi_payment_voucher.payment_mode,
                'total_amount': rmi_payment_voucher.amount_shs,
                'date': rmi_payment_voucher.date,
            }
            receipt_serializer = SchoolFundReceiptSerializer(
                rmi_payment_voucher.school_fund_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

        # Update TuitionReceipt if linked
        elif rmi_payment_voucher.vote_head == 'tuition' and rmi_payment_voucher.tuition_receipt:
            receipt_data = {
                'account': 'tuition_account',
                'received_from': rmi_payment_voucher.account,
                'cash_bank': rmi_payment_voucher.payment_mode,
                'total_amount': rmi_payment_voucher.amount_shs,
                'date': rmi_payment_voucher.date,
            }
            receipt_serializer = TuitionReceiptSerializer(
                rmi_payment_voucher.tuition_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

    def perform_destroy(self, instance):
        # Delete linked OperationReceipt if exists
        if instance.operation_receipt:
            instance.operation_receipt.delete()

        # Delete linked SchoolFundReceipt if exists
        if instance.school_fund_receipt:
            instance.school_fund_receipt.delete()

        # Delete linked TuitionReceipt if exists
        if instance.tuition_receipt:
            instance.tuition_receipt.delete()

        instance.delete()