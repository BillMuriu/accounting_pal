from rest_framework import serializers
from .models import Student
from students.students_opening_balances.models import StudentOpeningBalance
from accounts.school_fund.school_fund_receipts.models import SchoolFundReceipt
from other_apps.term_periods.models import TermPeriod
from django.db.models import Sum

class StudentSerializer(serializers.ModelSerializer):
    admissionNumber = serializers.CharField(source='admission_number')
    firstName = serializers.CharField(source='first_name')
    lastName = serializers.CharField(source='last_name')
    dateOfBirth = serializers.DateTimeField(source='date_of_birth', input_formats=["%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ"])
    admissionDate = serializers.DateTimeField(source='admission_date', input_formats=["%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ"])
    gradeClassLevel = serializers.CharField(source='grade_class_level')
    guardiansName = serializers.CharField(source='guardians_name')
    guardiansPhoneNumber = serializers.CharField(source='guardians_phone_number')
    gender = serializers.ChoiceField(choices=Student.GENDER_CHOICES)  # Add the gender field

    # Change the names to match the method names
    opening_balance = serializers.SerializerMethodField()
    total_fees = serializers.SerializerMethodField()
    total_receipts = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'id', 
            'admissionNumber', 
            'firstName', 
            'lastName', 
            'dateOfBirth', 
            'gender',  # Include gender in fields
            'admissionDate', 
            'gradeClassLevel', 
            'guardiansName', 
            'guardiansPhoneNumber', 
            'opening_balance', 
            'total_fees', 
            'total_receipts', 
            'balance'
        ]

    def get_opening_balance(self, obj):
        opening_balance = StudentOpeningBalance.objects.filter(student=obj).first()
        if opening_balance:
            return opening_balance.balance
        return None

    def get_total_fees(self, obj):
        """
            Calculate the total fees for a student starting from their opening balance record.

            This method retrieves the student's opening balance and determines all term periods 
            that began on or after the date the opening balance was recorded. It then calculates 
            the sum of fees for these terms.

            Args:
                obj: The student object for which the total fees need to be calculated.

            Returns:
                float: The total fees from the relevant term periods, or None if the student 
                does not have an opening balance.
                
            Notes:
                - Ensures the calculation only includes terms after the student was added to the system.
                - Returns None if the student does not have an opening balance, indicating no fees can be calculated.
        """
        opening_balance = StudentOpeningBalance.objects.filter(student=obj).first()
        if not opening_balance:
            return None
        
        terms = TermPeriod.objects.filter(start_date__gte=opening_balance.date_recorded)
        total_fees = sum(term.fees for term in terms)
        return total_fees

    def get_total_receipts(self, obj):
        total_receipts = SchoolFundReceipt.objects.filter(student=obj).aggregate(
            total_amount=Sum('total_amount')
        )['total_amount'] or 0
        return total_receipts

    def get_balance(self, obj):
        opening_balance = self.get_opening_balance(obj)
        if opening_balance is None:
            return None
        
        total_fees = self.get_total_fees(obj)
        total_receipts = self.get_total_receipts(obj)

        balance = (opening_balance + total_fees) - total_receipts
        return balance
