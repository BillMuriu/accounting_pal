# urls.py
from django.urls import path
from .views import PettyCashListCreateView, PettyCashRetrieveUpdateDestroyView

urlpatterns = [

    path('', PettyCashListCreateView.as_view(), name='petty-cash-list-create'),
    path('<int:pk>/', PettyCashRetrieveUpdateDestroyView.as_view(), name='petty-cash-detail'),
]
