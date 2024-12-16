from rest_framework import generics
from .models import TuitionPaymentVoucher
from .serializers import TuitionPaymentVoucherSerializer
from accounts.operations.operations_receipts.serializers import OperationReceiptSerializer

from rest_framework import generics
from .models import TuitionPaymentVoucher
from .serializers import TuitionPaymentVoucherSerializer
from accounts.operations.operations_receipts.serializers import OperationReceiptSerializer
from accounts.rmi.rmi_receipts.serializers import RMIReceiptSerializer
from accounts.school_fund.school_fund_receipts.serializers import SchoolFundReceiptSerializer


class ListCreateTuitionPaymentVoucherView(generics.ListCreateAPIView):
    queryset = TuitionPaymentVoucher.objects.all()
    serializer_class = TuitionPaymentVoucherSerializer

    def perform_create(self, serializer):
        # Save the TuitionPaymentVoucher instance
        tuition_payment_voucher = serializer.save()

        # If the vote head is 'operations', create a corresponding OperationReceipt
        if tuition_payment_voucher.vote_head == 'operations':
            receipt_data = {
                'account': 'operations_account',
                'received_from': tuition_payment_voucher.account,
                'cash_bank': tuition_payment_voucher.payment_mode,
                'total_amount': tuition_payment_voucher.amount_shs,
                'date': tuition_payment_voucher.date,
            }
            receipt_serializer = OperationReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                tuition_payment_voucher.operation_receipt = receipt
                tuition_payment_voucher.save()

        # If the vote head is 'school_fund', create a corresponding SchoolFundReceipt
        elif tuition_payment_voucher.vote_head == 'school_fund':
            receipt_data = {
                'account': 'school_fund_account',
                'received_from': tuition_payment_voucher.account,
                'cash_bank': tuition_payment_voucher.payment_mode,
                'total_amount': tuition_payment_voucher.amount_shs,
                'date': tuition_payment_voucher.date,
            }
            receipt_serializer = SchoolFundReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                tuition_payment_voucher.school_fund_receipt = receipt
                tuition_payment_voucher.save()

        # If the vote head is 'rmi', create a corresponding RMIReceipt
        elif tuition_payment_voucher.vote_head == 'rmi':
            receipt_data = {
                'account': 'rmi_account',
                'received_from': tuition_payment_voucher.account,
                'cash_bank': tuition_payment_voucher.payment_mode,
                'total_amount': tuition_payment_voucher.amount_shs,
                'date': tuition_payment_voucher.date,
            }
            receipt_serializer = RMIReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                tuition_payment_voucher.rmi_receipt = receipt
                tuition_payment_voucher.save()


class TuitionPaymentVoucherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TuitionPaymentVoucher.objects.all()
    serializer_class = TuitionPaymentVoucherSerializer

    def perform_update(self, serializer):
        tuition_payment_voucher = serializer.save()

        # Update OperationReceipt if linked
        if tuition_payment_voucher.vote_head == 'operations' and tuition_payment_voucher.operation_receipt:
            receipt_data = {
                'account': 'operations_account',
                'received_from': tuition_payment_voucher.account,
                'cash_bank': tuition_payment_voucher.payment_mode,
                'total_amount': tuition_payment_voucher.amount_shs,
                'date': tuition_payment_voucher.date,
            }
            receipt_serializer = OperationReceiptSerializer(
                tuition_payment_voucher.operation_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

        # Update SchoolFundReceipt if linked
        elif tuition_payment_voucher.vote_head == 'school_fund' and tuition_payment_voucher.school_fund_receipt:
            receipt_data = {
                'account': 'school_fund_account',
                'received_from': tuition_payment_voucher.account,
                'cash_bank': tuition_payment_voucher.payment_mode,
                'total_amount': tuition_payment_voucher.amount_shs,
                'date': tuition_payment_voucher.date,
            }
            receipt_serializer = SchoolFundReceiptSerializer(
                tuition_payment_voucher.school_fund_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

        # Update RMIReceipt if linked
        elif tuition_payment_voucher.vote_head == 'rmi' and tuition_payment_voucher.rmi_receipt:
            receipt_data = {
                'account': 'rmi_account',
                'received_from': tuition_payment_voucher.account,
                'cash_bank': tuition_payment_voucher.payment_mode,
                'total_amount': tuition_payment_voucher.amount_shs,
                'date': tuition_payment_voucher.date,
            }
            receipt_serializer = RMIReceiptSerializer(
                tuition_payment_voucher.rmi_receipt, data=receipt_data
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

        # Delete linked RMIReceipt if exists
        if instance.rmi_receipt:
            instance.rmi_receipt.delete()

        instance.delete()
