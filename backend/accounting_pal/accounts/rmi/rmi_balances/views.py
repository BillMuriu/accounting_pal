from rest_framework import generics, status
from .models import RMIOpeningBalance
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from datetime import datetime
from .serializers import RmiOpeningBalanceSerializer, RmiRunningBalanceSerializer, RmiBalanceCarriedForwardSerializer
from .utils import calculate_rmi_balance_carried_forward, calculate_rmi_running_balance


class RmiRunningBalanceView(APIView):
    def get(self, request, *args, **kwargs):
        account = request.query_params.get('account', 'rmi')  # Default to 'rmi' if not provided

        # Set the current date to now
        current_date = timezone.now().date()

        # Calculate running balance
        try:
            running_balance = calculate_rmi_running_balance(account)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize and return the response
        serializer = RmiRunningBalanceSerializer(running_balance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RmiBalanceCarriedForwardView(APIView):
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
            balance_carried_forward = calculate_rmi_balance_carried_forward(year, month)  # Remove account argument
        except ValueError:
            return Response({"detail": "Invalid date format. Please use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize and return the response
        serializer = RmiBalanceCarriedForwardSerializer(balance_carried_forward)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RmiOpeningBalanceListCreateView(generics.ListCreateAPIView):
    queryset = RMIOpeningBalance.objects.all()
    serializer_class = RmiOpeningBalanceSerializer

class RmiOpeningBalanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RMIOpeningBalance.objects.all()
    serializer_class = RmiOpeningBalanceSerializer
