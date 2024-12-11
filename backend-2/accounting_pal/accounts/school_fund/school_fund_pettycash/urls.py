from django.urls import path
from .views import SchoolFundPettyCashListCreateView, SchoolFundPettyCashRetrieveUpdateDestroyView

urlpatterns = [
    path('', SchoolFundPettyCashListCreateView.as_view(), name='schoolfundpettycash-list-create'),
    path('<int:pk>/', SchoolFundPettyCashRetrieveUpdateDestroyView.as_view(), name='schoolfundpettycash-detail'),
]
