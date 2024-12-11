from rest_framework import generics
from .models import SchoolFundPaymentVoucher
from .serializers import SchoolFundPaymentVoucherSerializer
from accounts.operations.operations_receipts.models import OperationReceipt
from accounts.operations.operations_receipts.serializers import OperationReceiptSerializer

class ListCreateSchoolFundPaymentVoucherView(generics.ListCreateAPIView):
    queryset = SchoolFundPaymentVoucher.objects.all()
    serializer_class = SchoolFundPaymentVoucherSerializer

    def perform_create(self, serializer):
        # Save the SchoolFundPaymentVoucher instance
        school_fund_payment_voucher = serializer.save()

        # Debugging: Log the saved payment voucher
        print(f"Saved SchoolFundPaymentVoucher: {school_fund_payment_voucher}")

        # Create an OperationReceipt instance using the data from the payment voucher
        operation_receipt_data = {
            'account': 'operations_account',  # Default value
            'receivedFrom': 'school_fund',    # Changed to camelCase
            'cashBank': school_fund_payment_voucher.payment_mode,  # Changed to camelCase
            'totalAmount': school_fund_payment_voucher.amount_shs,  # Changed to camelCase
            'date': school_fund_payment_voucher.date,
            # Explicitly set rmiFund and otherVoteheads to None
            'rmiFund': None,
            'otherVoteheads': None,
        }

        # Debugging: Log the operation receipt data being created
        print(f"Creating OperationReceipt with data: {operation_receipt_data}")

        operation_receipt_serializer = OperationReceiptSerializer(data=operation_receipt_data)

        if operation_receipt_serializer.is_valid():
            operation_receipt = operation_receipt_serializer.save()
            # Link the OperationReceipt to the SchoolFundPaymentVoucher
            school_fund_payment_voucher.operation_receipt = operation_receipt
            school_fund_payment_voucher.save()
            print(f"Successfully created OperationReceipt: {operation_receipt}")
        else:
            # Handle serializer errors if needed
            print("OperationReceiptSerializer errors:", operation_receipt_serializer.errors)

class SchoolFundPaymentVoucherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolFundPaymentVoucher.objects.all()
    serializer_class = SchoolFundPaymentVoucherSerializer

    def perform_update(self, serializer):
        # Save the updated payment voucher instance
        school_fund_payment_voucher = serializer.save()
        print(f'Updated School Fund Payment Voucher: {school_fund_payment_voucher}')

        # If there's an associated OperationReceipt, update it as necessary
        if school_fund_payment_voucher.operation_receipt:
            operation_receipt_data = {
                'account': 'operations_account',
                'receivedFrom': 'school_fund',  # Changed to camelCase
                'cashBank': school_fund_payment_voucher.payment_mode,  # Changed to camelCase
                'totalAmount': school_fund_payment_voucher.amount_shs,  # Changed to camelCase
                'date': school_fund_payment_voucher.date,
                # Explicitly set rmiFund and otherVoteheads to None if they're not provided
                'rmiFund': None,
                'otherVoteheads': None,
            }
            operation_receipt_serializer = OperationReceiptSerializer(
                school_fund_payment_voucher.operation_receipt, data=operation_receipt_data
            )
            if operation_receipt_serializer.is_valid():
                operation_receipt_serializer.save()
                print(f'Updated Operation Receipt: {school_fund_payment_voucher.operation_receipt}')
            else:
                print(f'Operation Receipt Serializer Errors on Update: {operation_receipt_serializer.errors}')

    def perform_destroy(self, instance):
        # If there's an associated OperationReceipt, delete it
        if instance.operation_receipt:
            instance.operation_receipt.delete()
            print(f'Deleted Operation Receipt: {instance.operation_receipt}')
        instance.delete()
        print(f'Deleted School Fund Payment Voucher: {instance}')


class ListSchoolFundPaymentVoucherView(generics.ListAPIView):
    queryset = SchoolFundPaymentVoucher.objects.all()
    serializer_class = SchoolFundPaymentVoucherSerializer


class RetrieveSchoolFundPaymentVoucherView(generics.RetrieveAPIView):
    queryset = SchoolFundPaymentVoucher.objects.all()
    serializer_class = SchoolFundPaymentVoucherSerializer
