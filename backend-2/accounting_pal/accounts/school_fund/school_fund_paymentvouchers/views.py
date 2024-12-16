from rest_framework import generics
from .models import SchoolFundPaymentVoucher
from .serializers import SchoolFundPaymentVoucherSerializer
from accounts.operations.operations_receipts.serializers import OperationReceiptSerializer
from accounts.rmi.rmi_receipts.serializers import RMIReceiptSerializer
from accounts.tuition.tuition_receipts.serializers import TuitionReceiptSerializer


class ListCreateSchoolFundPaymentVoucherView(generics.CreateAPIView):
    queryset = SchoolFundPaymentVoucher.objects.all()
    serializer_class = SchoolFundPaymentVoucherSerializer

    def perform_create(self, serializer):
        payment_voucher = serializer.save()

        # Handle Operations Receipt Creation
        if payment_voucher.vote_head == 'operations':
            receipt_data = {
                'account': 'operations_account',
                'received_from': 'school_fund',  # The fund creating this payment voucher
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = OperationReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                payment_voucher.operations_receipt = receipt
                payment_voucher.save()

        # Handle RMI Receipt Creation
        elif payment_voucher.vote_head == 'rmi':
            receipt_data = {
                'account': 'rmi_account',
                'received_from': 'school_fund',
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = RMIReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                payment_voucher.rmi_receipt = receipt
                payment_voucher.save()

        # Handle Tuition Receipt Creation
        elif payment_voucher.vote_head == 'tuition':
            receipt_data = {
                'account': 'tuition_account',
                'received_from': 'school_fund',
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = TuitionReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                payment_voucher.tuition_receipt = receipt
                payment_voucher.save()


class SchoolFundPaymentVoucherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolFundPaymentVoucher.objects.all()
    serializer_class = SchoolFundPaymentVoucherSerializer

    def perform_update(self, serializer):
        payment_voucher = serializer.save()

        # Update Operations Receipt if linked
        if payment_voucher.vote_head == 'operations' and payment_voucher.operations_receipt:
            receipt_data = {
                'account': 'operations_account',
                'received_from': 'school_fund',
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = OperationReceiptSerializer(
                payment_voucher.operations_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

        # Update RMI Receipt if linked
        elif payment_voucher.vote_head == 'rmi' and payment_voucher.rmi_receipt:
            receipt_data = {
                'account': 'rmi_account',
                'received_from': 'school_fund',
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = RMIReceiptSerializer(
                payment_voucher.rmi_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

        # Update Tuition Receipt if linked
        elif payment_voucher.vote_head == 'tuition' and payment_voucher.tuition_receipt:
            receipt_data = {
                'account': 'tuition_account',
                'received_from': 'school_fund',
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = TuitionReceiptSerializer(
                payment_voucher.tuition_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

    def perform_destroy(self, instance):
        # Delete linked Operation Receipt if exists
        if instance.operations_receipt:
            instance.operations_receipt.delete()

        # Delete linked RMI Receipt if exists
        if instance.rmi_receipt:
            instance.rmi_receipt.delete()

        # Delete linked Tuition Receipt if exists
        if instance.tuition_receipt:
            instance.tuition_receipt.delete()

        instance.delete()


class ListSchoolFundPaymentVoucherView(generics.ListAPIView):
    queryset = SchoolFundPaymentVoucher.objects.all()
    serializer_class = SchoolFundPaymentVoucherSerializer


class RetrieveSchoolFundPaymentVoucherView(generics.RetrieveAPIView):
    queryset = SchoolFundPaymentVoucher.objects.all()
    serializer_class = SchoolFundPaymentVoucherSerializer
