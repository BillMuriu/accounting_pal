from django.db import models
from students.students.models import Student

class StudentOpeningBalance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text="The student associated with this opening balance")
    balance = models.DecimalField(max_digits=10, decimal_places=2, help_text="The opening balance amount for the student")
    date_recorded = models.DateField(help_text="Date when the opening balance was recorded")

    def __str__(self):
        return f"{self.student} - Opening Balance: {self.balance}"
