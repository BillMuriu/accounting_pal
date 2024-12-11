from rest_framework import generics
from .models import RMIPaymentVoucher
from .serializers import RMIPaymentVoucherSerializer
from accounts.operations.operations_receipts.serializers import OperationReceiptSerializer

class ListCreateRMIPaymentVoucherView(generics.ListCreateAPIView):
    queryset = RMIPaymentVoucher.objects.all()
    serializer_class = RMIPaymentVoucherSerializer

    def perform_create(self, serializer):
        # Save the RMIPaymentVoucher instance
        rmi_payment_voucher = serializer.save()

        # Debugging: Log the saved payment voucher
        print(f"Saved RMIPaymentVoucher: {rmi_payment_voucher}")

        # Only create an OperationReceipt if the vote_head is 'operations'
        if rmi_payment_voucher.vote_head == 'operations':
            # Create an OperationReceipt instance using the data from the payment voucher
            operation_receipt_data = {
                'account': 'operations_account',  # Default value
                'receivedFrom': 'rmi',            # Changed to camelCase
                'cashBank': rmi_payment_voucher.payment_mode,  # Changed to camelCase
                'totalAmount': rmi_payment_voucher.amount_shs,  # Changed to camelCase
                'date': rmi_payment_voucher.date,
                # Explicitly set schoolFund and otherVoteheads to None
                'rmiFund': None,
                'schoolFund': None,
                'otherVoteheads': None,
            }

            # Debugging: Log the operation receipt data being created
            print(f"Creating OperationReceipt with data: {operation_receipt_data}")

            operation_receipt_serializer = OperationReceiptSerializer(data=operation_receipt_data)

            if operation_receipt_serializer.is_valid():
                operation_receipt = operation_receipt_serializer.save()
                # Link the OperationReceipt to the RMIPaymentVoucher
                rmi_payment_voucher.operation_receipt = operation_receipt
                rmi_payment_voucher.save()
                print(f"Successfully created OperationReceipt: {operation_receipt}")
            else:
                # Handle serializer errors if needed
                print("OperationReceiptSerializer errors:", operation_receipt_serializer.errors)

class RMIPaymentVoucherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RMIPaymentVoucher.objects.all()
    serializer_class = RMIPaymentVoucherSerializer

    def perform_update(self, serializer):
        # Save the updated payment voucher instance
        rmi_payment_voucher = serializer.save()
        print(f'Updated RMI Payment Voucher: {rmi_payment_voucher}')

        # If there's an associated OperationReceipt, update it as necessary
        if rmi_payment_voucher.operation_receipt:
            operation_receipt_data = {
                'account': 'operations_account',
                'receivedFrom': 'rmi',            # Changed to camelCase
                'cashBank': rmi_payment_voucher.payment_mode,  # Changed to camelCase
                'totalAmount': rmi_payment_voucher.amount_shs,  # Changed to camelCase
                'date': rmi_payment_voucher.date,
                # Explicitly set schoolFund and otherVoteheads to None if they're not provided
                'schoolFund': None,
                'otherVoteheads': None,
            }
            operation_receipt_serializer = OperationReceiptSerializer(
                rmi_payment_voucher.operation_receipt, data=operation_receipt_data
            )
            if operation_receipt_serializer.is_valid():
                operation_receipt_serializer.save()
                print(f'Updated Operation Receipt: {rmi_payment_voucher.operation_receipt}')
            else:
                print(f'Operation Receipt Serializer Errors on Update: {operation_receipt_serializer.errors}')

    def perform_destroy(self, instance):
        # If there's an associated OperationReceipt, delete it
        if instance.operation_receipt:
            instance.operation_receipt.delete()
            print(f'Deleted Operation Receipt: {instance.operation_receipt}')
        instance.delete()
        print(f'Deleted RMI Payment Voucher: {instance}')
