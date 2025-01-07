# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .cashbook_utils import (
    get_school_fund_payments_money_out,
    get_school_fund_receipts_money_in,
    get_school_fund_cashbook
)


class SchoolFundPaymentsMoneyOutView(APIView):
    def get(self, request, *args, **kwargs):
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if not year or not month:
            return Response({"error": "Year and month parameters are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year = int(year)
            month = int(month)
            payments_data = get_school_fund_payments_money_out(year, month)  # Updated function name
            return Response(payments_data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid year or month format."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SchoolFundReceiptsMoneyInView(APIView):
    def get(self, request):
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        if month is None or year is None:
            return Response({"error": "Both 'month' and 'year' query parameters are required."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            month = int(month)
            year = int(year)
            receipts_data = get_school_fund_receipts_money_in(year, month)  # Updated function name
            return Response(receipts_data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid month or year format."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SchoolFundCashbookView(APIView):
    def get(self, request, *args, **kwargs):
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if not year or not month:
            return Response({"error": "Year and month parameters are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year = int(year)
            month = int(month)
            cashbook_data = get_school_fund_cashbook(year, month)  # Updated function name
            return Response(cashbook_data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid year or month format."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
