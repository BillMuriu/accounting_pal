"""
URL configuration for accounting_pal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
# operations urls
    path('admin/', admin.site.urls),
    path('api/operations-receipts/', include('accounts.operations.operations_receipts.urls')),
    path('api/operations-paymentvouchers/', include('accounts.operations.operations_paymentvouchers.urls')),
    path('api/operations-pettycash/', include('accounts.operations.operations_pettycash.urls')),
    path('api/operations-bankcharges/', include('accounts.operations.operations_bankcharges.urls')),
    path('api/operations-balances/', include('accounts.operations.operations_balances.urls')),
    path('api/operations-cashbooks/', include('accounts.operations.operations_cashbooks.urls')),
    path('api/operations-ledgers/', include('accounts.operations.operations_ledgers.urls')),
    path('api/operations-trialbalances/', include('accounts.operations.operations_trial_balance.urls')),

# Rmi urls
    path('api/rmi-receipts/', include('accounts.rmi.rmi_receipts.urls')),
    path('api/rmi-petty-cash/', include('accounts.rmi.rmi_pettycash.urls')),
    path('api/rmi-payment-vouchers/', include('accounts.rmi.rmi_paymentvoucher.urls')),
    path('api/rmi-bank-charges/', include('accounts.rmi.rmi_bankcharges.urls')),
    path('api/rmi-balances/', include('accounts.rmi.rmi_balances.urls')),
    path('api/rmi-cashbooks/', include('accounts.rmi.rmi_cashbook.urls')),
    path('api/rmi-ledgers/', include('accounts.rmi.rmi_ledgers.urls')),
    path('api/rmi-trialbalances/', include('accounts.rmi.rmi_trial_balance.urls')),


# Tuition urls
    path('api/tuition-receipts/', include('accounts.tuition.tuition_receipts.urls')),
    path('api/tuition-pettycash/', include('accounts.tuition.tuition_pettycash.urls')),
    path('api/tuition-payment-vouchers/', include('accounts.tuition.tuition_paymentvouchers.urls')),
    path('api/tuition-bank-charges/', include('accounts.tuition.tuition_bankcharges.urls')),
    path('api/tuition-balances/', include('accounts.tuition.tuition_balances.urls')),
    path('api/tuition-cashbooks/', include('accounts.tuition.tuition_cashbooks.urls')),
    path('api/tuition-ledgers/', include('accounts.tuition.tuition_ledgers.urls')),



# student urls
    path('api/students/', include('students.students.urls')),
    path('api/students_opening_balances/', include('students.students_opening_balances.urls')),

# term_periods urls
    path('api/term_periods/', include('other_apps.term_periods.urls')),

# school fund urls
    path('api/school_fund_receipts/', include('accounts.school_fund.school_fund_receipts.urls')),
    path('api/school-fund-petty-cash/', include('accounts.school_fund.school_fund_pettycash.urls')),
    path('api/school-fund-payment-vouchers/', include('accounts.school_fund.school_fund_paymentvouchers.urls')),
    path('api/school-fund-bank-charges/', include('accounts.school_fund.school_fund_bankcharge.urls')),

# custom_auth
    path('api/custom_auth/', include('custom_auth.urls')),

]
