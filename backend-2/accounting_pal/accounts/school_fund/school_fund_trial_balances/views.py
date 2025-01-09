# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from .utils.balances_utils import calculate_school_fund_balances
from .utils.create_trial_balance_utils import create_school_fund_trial_balance


class CalculateSchoolFundBalancesView(APIView):
    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        # Validate the input
        if not start_date_str or not end_date_str:
            return Response(
                {"error": "Please provide start_date and end_date."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Parse the dates
        start_date = parse_datetime(start_date_str)
        end_date = parse_datetime(end_date_str)

        if not start_date or not end_date:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Make sure the dates are timezone-aware
        if timezone.is_naive(start_date):
            start_date = timezone.make_aware(start_date)
        if timezone.is_naive(end_date):
            end_date = timezone.make_aware(end_date)

        # Call the calculate_school_fund_balances function
        try:
            balances = calculate_school_fund_balances(start_date, end_date)
            return Response(balances, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class SchoolFundTrialBalanceView(APIView):
    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response(
                {"error": "Please provide start_date and end_date."},
                status=status.HTTP_400_BAD_REQUEST
            )

        start_date = parse_datetime(start_date_str)
        end_date = parse_datetime(end_date_str)

        if not start_date or not end_date:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if timezone.is_naive(start_date):
            start_date = timezone.make_aware(start_date)
        if timezone.is_naive(end_date):
            end_date = timezone.make_aware(end_date)

        # Call the create_school_fund_trial_balance function
        try:
            trial_balance = create_school_fund_trial_balance(start_date, end_date)
            return Response(trial_balance, status=status.HTTP_200_OK)
        except KeyError as e:
            return Response(
                {"error": f"Missing key in response: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
