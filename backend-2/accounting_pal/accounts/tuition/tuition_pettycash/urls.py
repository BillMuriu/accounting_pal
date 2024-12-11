from django.urls import path
from .views import TuitionPettyCashListCreateView, TuitionPettyCashRetrieveUpdateDestroyView

urlpatterns = [
    path('', TuitionPettyCashListCreateView.as_view(), name='tuition-pettycash-list-create'),
    path('<int:id>/', TuitionPettyCashRetrieveUpdateDestroyView.as_view(), name='tuition-pettycash-retrieve-update-destroy'),
]
