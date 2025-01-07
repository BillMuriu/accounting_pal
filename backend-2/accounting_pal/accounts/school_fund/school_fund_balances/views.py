from rest_framework import generics, status
from .models import SchoolFundOpeningBalance  # Update the model import
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import datetime
from .serializers import SchoolFundOpeningBalanceSerializer, RunningSchoolFundBalanceSerializer, SchoolFundBalanceCarriedForwardSerializer
from .utils import calculate_running_balance, calculate_balance_carried_forward

class RunningBalanceView(APIView):
    def get(self, request, *args, **kwargs):
        account = request.query_params.get('account', 'school_fund')  # Default to 'school_fund' for School Fund account

        # Set the current date to now
        current_date = timezone.now().date()

        try:
            # Call the utility function with the correct account
            running_balance = calculate_running_balance(account)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize and return the response
        serializer = RunningSchoolFundBalanceSerializer(running_balance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BalanceCarriedForwardView(APIView):
    def get(self, request, *args, **kwargs):
        date_str = request.query_params.get('date')

        if not date_str:
            return Response({"detail": "Date query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Parse the date and extract the year and month
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            year = date_obj.year
            month = date_obj.month

            # Calculate balance carried forward without account argument
            balance_carried_forward = calculate_balance_carried_forward(year, month)  # Remove account argument for School Fund
        except ValueError:
            return Response({"detail": "Invalid date format. Please use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize and return the response
        serializer = SchoolFundBalanceCarriedForwardSerializer(balance_carried_forward)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SchoolFundOpeningBalanceListCreateView(generics.ListCreateAPIView):  # Update the view name
    queryset = SchoolFundOpeningBalance.objects.all()  # Update the model reference
    serializer_class = SchoolFundOpeningBalanceSerializer  # Use the correct serializer


class SchoolFundOpeningBalanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):  # Update the view name
    queryset = SchoolFundOpeningBalance.objects.all()  # Update the model reference
    serializer_class = SchoolFundOpeningBalanceSerializer  # Use the correct serializer
