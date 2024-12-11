from rest_framework import generics
from .models import TuitionPaymentVoucher
from .serializers import TuitionPaymentVoucherSerializer
from accounts.operations.operations_receipts.serializers import OperationReceiptSerializer

class ListCreateTuitionPaymentVoucherView(generics.ListCreateAPIView):
    queryset = TuitionPaymentVoucher.objects.all()
    serializer_class = TuitionPaymentVoucherSerializer

    def perform_create(self, serializer):
        # Save the TuitionPaymentVoucher instance
        tuition_payment_voucher = serializer.save()

        # Debugging: Log the saved payment voucher
        print(f"Saved TuitionPaymentVoucher: {tuition_payment_voucher}")

        # Only create an OperationReceipt if the vote_head is 'tuition'
        if tuition_payment_voucher.vote_head == 'operations':
            # Create an OperationReceipt instance using the data from the payment voucher
            operation_receipt_data = {
                'account': 'operations_account',  # Default value for tuition account
                'receivedFrom': 'tuition',         # Changed to camelCase
                'cashBank': tuition_payment_voucher.payment_mode,  # Changed to camelCase
                'totalAmount': tuition_payment_voucher.amount_shs,  # Changed to camelCase
                'date': tuition_payment_voucher.date,
                # Explicitly set other fields to None if not applicable
                'rmiFund': None,
                'schoolFund': None,
                'otherVoteheads': None,
            }

            # Debugging: Log the operation receipt data being created
            print(f"Creating OperationReceipt with data: {operation_receipt_data}")

            operation_receipt_serializer = OperationReceiptSerializer(data=operation_receipt_data)

            if operation_receipt_serializer.is_valid():
                operation_receipt = operation_receipt_serializer.save()
                # Link the OperationReceipt to the TuitionPaymentVoucher
                tuition_payment_voucher.operation_receipt = operation_receipt
                tuition_payment_voucher.save()
                print(f"Successfully created OperationReceipt: {operation_receipt}")
            else:
                # Handle serializer errors if needed
                print("OperationReceiptSerializer errors:", operation_receipt_serializer.errors)

class TuitionPaymentVoucherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TuitionPaymentVoucher.objects.all()
    serializer_class = TuitionPaymentVoucherSerializer

    def perform_update(self, serializer):
        # Save the updated payment voucher instance
        tuition_payment_voucher = serializer.save()
        print(f'Updated Tuition Payment Voucher: {tuition_payment_voucher}')

        # If there's an associated OperationReceipt, update it as necessary
        if tuition_payment_voucher.operation_receipt:
            operation_receipt_data = {
                'account': 'tuition_account',  # Default value for tuition account
                'receivedFrom': 'rmi',         # Changed to camelCase
                'cashBank': tuition_payment_voucher.payment_mode,  # Changed to camelCase
                'totalAmount': tuition_payment_voucher.amount_shs,  # Changed to camelCase
                'date': tuition_payment_voucher.date,
                # Explicitly set other fields to None if they're not provided
                'rmiFund': None,
                'schoolFund': None,
                'otherVoteheads': None,
            }
            operation_receipt_serializer = OperationReceiptSerializer(
                tuition_payment_voucher.operation_receipt, data=operation_receipt_data
            )
            if operation_receipt_serializer.is_valid():
                operation_receipt_serializer.save()
                print(f'Updated Operation Receipt: {tuition_payment_voucher.operation_receipt}')
            else:
                print(f'Operation Receipt Serializer Errors on Update: {operation_receipt_serializer.errors}')

    def perform_destroy(self, instance):
        # If there's an associated OperationReceipt, delete it
        if instance.operation_receipt:
            instance.operation_receipt.delete()
            print(f'Deleted Operation Receipt: {instance.operation_receipt}')
        instance.delete()
        print(f'Deleted Tuition Payment Voucher: {instance}')
