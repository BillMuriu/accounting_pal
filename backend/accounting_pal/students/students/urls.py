# urls.py
from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDestroyView

urlpatterns = [
    path('', StudentListCreateView.as_view(), name='student-list-create'),
    path('<int:id>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),

    # path('<int:student_id>/balance/', StudentBalanceView.as_view(), name='student-balance'),

]
