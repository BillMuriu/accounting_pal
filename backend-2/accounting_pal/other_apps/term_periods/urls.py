# urls.py
from django.urls import path
from .views import TermPeriodListCreateView, TermPeriodRetrieveUpdateDestroyView

urlpatterns = [
    path('', TermPeriodListCreateView.as_view(), name='termperiod-list-create'),
    path('<int:id>/', TermPeriodRetrieveUpdateDestroyView.as_view(), name='termperiod-detail'),
]
