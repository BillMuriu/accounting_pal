from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.utils import timezone
from .utils.bank_charge_ledger_utils import get_school_fund_bankcharge_ledger
from .utils.rmi_ledger_utils import get_school_fund_rmi_ledger
from .utils.tuition_ledger_utils import get_school_fund_tuition_ledger
from .utils.other_voteheads_ledger_utils import get_school_fund_other_voteheads_ledger
from .utils.operations_ledger_utils import get_operations_ledger

class SchoolFundRMILedgerView(APIView):
    def get(self, request, *args, **kwargs):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        ledger = get_school_fund_rmi_ledger(start_date, end_date)
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)


class SchoolFundBankChargeLedgerView(APIView):
    def get(self, request, *args, **kwargs):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        ledger = get_school_fund_bankcharge_ledger(start_date, end_date)
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)


class SchoolFundTuitionLedgerView(APIView):
    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = timezone.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = timezone.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        ledger = get_school_fund_tuition_ledger(start_date, end_date)
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)


class SchoolFundOtherVoteheadsLedgerView(APIView):
    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = timezone.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = timezone.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        ledger = get_school_fund_other_voteheads_ledger(start_date, end_date)
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)


class SchoolFundCombinedLedgerView(APIView):
    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        rmi_ledger = get_school_fund_rmi_ledger(start_date, end_date)
        bank_charge_ledger = get_school_fund_bankcharge_ledger(start_date, end_date)
        tuition_ledger = get_school_fund_tuition_ledger(start_date, end_date)
        other_voteheads_ledger = get_school_fund_other_voteheads_ledger(start_date, end_date)

        combined_ledger = {
            "rmi_ledger": rmi_ledger,
            "bank_charge_ledger": bank_charge_ledger,
            "tuition_ledger": tuition_ledger,
            "other_voteheads_ledger": other_voteheads_ledger,
        }

        return Response({"combined_ledger": combined_ledger}, status=status.HTTP_200_OK)

class SchoolFundOperationsLedgerView(APIView):
    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = timezone.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = timezone.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        ledger = get_operations_ledger(start_date, end_date)
        return Response({"ledger": ledger}, status=status.HTTP_200_OK)
