from django.urls import path
from .views import RequestMagicLinkView, VerifyMagicLinkView

urlpatterns = [
    path('send-magic-link/', RequestMagicLinkView.as_view(), name='send-magic-link'),
    path('verify-magic-link/', VerifyMagicLinkView.as_view(), name='verify-magic-link'),
]
