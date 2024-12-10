from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from datetime import datetime
from.utils.rmi_ledger_utils import get_rmi_ledger
from .utils.bank_charge_ledger_utils import get_bankcharge_ledger
from .utils.schoolfund_ledger_utils import get_school_fund_ledger
from .utils.tuition_ledger_utils import get_tuition_ledger
from .utils.other_voteheads_ledger_utils import get_other_voteheads_ledger


class RMILedgerView(APIView):
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

        # Call the function to get the RMI ledger
        ledger = get_rmi_ledger(start_date, end_date)

        # Return the ledger in the response
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)



class SchoolFundLedgerView(APIView):
    def get(self, request):
        # Get start_date and end_date from query parameters
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response(
                {"error": "start_date and end_date are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Parse the date strings to datetime objects
            start_date = timezone.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = timezone.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get the ledger data
        ledger = get_school_fund_ledger(start_date, end_date)

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

        # Return the ledger (with debits and total) in the response
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)


class TuitionLedgerView(APIView):
    def get(self, request):
        # Get start_date and end_date from query parameters
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response(
                {"error": "start_date and end_date are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Parse the date strings to datetime objects
            start_date = timezone.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = timezone.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get the ledger data
        ledger = get_tuition_ledger(start_date, end_date)

        return Response({"ledger": ledger}, status=status.HTTP_200_OK)
    

class OtherVoteheadsLedgerView(APIView):
    def get(self, request):
        # Get start_date and end_date from query parameters
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response(
                {"error": "start_date and end_date are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Parse the date strings to datetime objects
            start_date = timezone.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = timezone.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get the ledger data
        ledger = get_other_voteheads_ledger(start_date, end_date)

        return Response({"ledger": ledger}, status=status.HTTP_200_OK)