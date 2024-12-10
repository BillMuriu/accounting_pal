from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils.operations_ledger_utils import get_operations_ledger
from .utils.other_voteheads_ledger_utils import get_other_voteheads_ledger
from .utils.schoolfund_ledger_utils import get_schoolfund_ledger
from .utils.tuition_ledger_utils import get_tuition_ledger
from .utils.bank_charge_ledger_utils import get_bankcharge_ledger


class OperationsLedgerView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract start_date and end_date from query parameters
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        # Ensure both start_date and end_date are provided
        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convert strings to datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        # Call the function to get the operations ledger
        ledger = get_operations_ledger(start_date, end_date)

        # Return the ledger in the response
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)


class OtherVoteheadsLedgerView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract start_date and end_date from query parameters
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        # Ensure both start_date and end_date are provided
        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convert strings to datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        # Call the function to get the other voteheads ledger
        ledger = get_other_voteheads_ledger(start_date, end_date)

        # Return the ledger in the response
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)
    

class SchoolFundLedgerView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract start_date and end_date from query parameters
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        # Ensure both start_date and end_date are provided
        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convert strings to datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        # Call the function to get the school fund ledger
        ledger = get_schoolfund_ledger(start_date, end_date)

        # Return the ledger in the response
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)
    

class TuitionLedgerView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract start_date and end_date from query parameters
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        # Ensure both start_date and end_date are provided
        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convert strings to datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        # Call the function to get the tuition ledger
        ledger = get_tuition_ledger(start_date, end_date)

        # Return the ledger in the response
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)
    

class BankChargeLedgerView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract start_date and end_date from query parameters
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        # Ensure both start_date and end_date are provided
        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convert strings to datetime objects
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        # Call the function to get the bank charge ledger
        ledger = get_bankcharge_ledger(start_date, end_date)

        # Return the ledger in the response
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)