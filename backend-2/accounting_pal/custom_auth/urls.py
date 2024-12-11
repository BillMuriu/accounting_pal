from django.urls import path
from .views import RequestMagicLinkView, CreateUserView, UserDetailAndDeleteView

urlpatterns = [
    path('send-magic-link/', RequestMagicLinkView.as_view(), name='send-magic-link'),
    path('user/<int:pk>/', UserDetailAndDeleteView.as_view(), name='user-detail-and-delete'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
]
