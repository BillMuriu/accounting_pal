from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .cashbook_utils import get_tuition_payments_money_out, get_tuition_receipts_money_in, get_tuition_cashbook

class TuitionPaymentsMoneyOutView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract the year and month from the request query parameters
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        # Validate the year and month
        if not year or not month:
            return Response({"error": "Year and month parameters are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year = int(year)
            month = int(month)
            # Call the utility function to fetch payments, passing year and month
            payments_data = get_tuition_payments_money_out(year, month)
            return Response(payments_data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid year or month format."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TuitionReceiptsMoneyInView(APIView):
    def get(self, request):
        # Get month and year from query parameters and convert to integers
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        # Ensure both month and year are provided
        if month is None or year is None:
            return Response({"error": "Both 'month' and 'year' query parameters are required."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            # Convert month and year to integers
            month = int(month)
            year = int(year)

            receipts_data = get_tuition_receipts_money_in(year, month)
            return Response(receipts_data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid month or year format."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TuitionCashbookView(APIView):
    def get(self, request, *args, **kwargs):
        # Extract the year and month from the request query parameters
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        # Validate the year and month
        if not year or not month:
            return Response({"error": "Year and month parameters are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year = int(year)
            month = int(month)
            # Call the utility function to fetch the cashbook data, passing year and month
            cashbook_data = get_tuition_cashbook(year, month)
            return Response(cashbook_data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({"error": "Invalid year or month format."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
