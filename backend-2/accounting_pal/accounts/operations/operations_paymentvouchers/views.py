# views.py
from rest_framework import generics
from .models import PaymentVoucher
from .serializers import PaymentVoucherSerializer
from accounts.school_fund.school_fund_receipts.serializers import SchoolFundReceiptSerializer
from accounts.rmi.rmi_receipts.serializers import RMIReceiptSerializer
from accounts.tuition.tuition_receipts.serializers import TuitionReceiptSerializer  # Import TuitionReceiptSerializer

class CreatePaymentVoucherView(generics.CreateAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

    def perform_create(self, serializer):
        payment_voucher = serializer.save()
        
        # If the vote head is 'school_fund', create a corresponding SchoolFundReceipt
        if payment_voucher.vote_head == 'school_fund':
            receipt_data = {
                'account': 'school_fund_account',
                'received_from': payment_voucher.account,
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = SchoolFundReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                payment_voucher.school_fund_receipt = receipt
                payment_voucher.save()

        # If the vote head is 'rmi', create a corresponding RMIReceipt
        elif payment_voucher.vote_head == 'rmi':
            receipt_data = {
                'account': 'rmi_account',
                'received_from': payment_voucher.account,
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = RMIReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                payment_voucher.rmi_receipt = receipt
                payment_voucher.save()

        # If the vote head is 'tuition', create a corresponding TuitionReceipt
        elif payment_voucher.vote_head == 'tuition':
            receipt_data = {
                'account': 'tuition_account',
                'received_from': payment_voucher.account,
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = TuitionReceiptSerializer(data=receipt_data)
            if receipt_serializer.is_valid():
                receipt = receipt_serializer.save()
                payment_voucher.tuition_receipt = receipt
                payment_voucher.save()


class PaymentVoucherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

    def perform_update(self, serializer):
        payment_voucher = serializer.save()

        # Update SchoolFundReceipt if linked
        if payment_voucher.vote_head == 'school_fund' and payment_voucher.school_fund_receipt:
            receipt_data = {
                'account': 'school_fund_account',
                'received_from': payment_voucher.account,
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = SchoolFundReceiptSerializer(
                payment_voucher.school_fund_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

        # Update RMIReceipt if linked
        elif payment_voucher.vote_head == 'rmi' and payment_voucher.rmi_receipt:
            receipt_data = {
                'account': 'rmi_account',
                'received_from': payment_voucher.account,
                'cash_bank': payment_voucher.payment_mode,
                'total_amount': payment_voucher.amount_shs,
                'date': payment_voucher.date,
            }
            receipt_serializer = RMIReceiptSerializer(
                payment_voucher.rmi_receipt, data=receipt_data
            )
            if receipt_serializer.is_valid():
                receipt_serializer.save()

        # Update TuitionReceipt if linked
        elif payment_voucher.vote_head == 'tuition' and payment_voucher.tuition_receipt:
            receipt_data = {
                'account': 'tuition_account',
                'received_from': payment_voucher.account,
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
        # Delete linked SchoolFundReceipt if exists
        if instance.school_fund_receipt:
            instance.school_fund_receipt.delete()

        # Delete linked RMIReceipt if exists
        if instance.rmi_receipt:
            instance.rmi_receipt.delete()

        # Delete linked TuitionReceipt if exists
        if instance.tuition_receipt:
            instance.tuition_receipt.delete()

        instance.delete()


class ListPaymentVoucherView(generics.ListAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

class RetrievePaymentVoucherView(generics.RetrieveAPIView):
    queryset = PaymentVoucher.objects.all()
    serializer_class = PaymentVoucherSerializer

