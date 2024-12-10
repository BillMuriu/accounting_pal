from django.db import models

class Student(models.Model):
    CLASS_CHOICES = [
        ('form1', 'Form 1'),
        ('form2', 'Form 2'),
        ('form3', 'Form 3'),
        ('form4', 'Form 4'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    admission_number = models.CharField(max_length=20, unique=True, help_text="Unique admission number for each student")
    first_name = models.CharField(max_length=50, help_text="Student's first name")
    last_name = models.CharField(max_length=50, help_text="Student's last name")
    date_of_birth = models.DateTimeField(help_text="Student's date of birth")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, help_text="Student's gender")
    admission_date = models.DateTimeField(auto_now_add=True, help_text="Date the student was admitted")
    grade_class_level = models.CharField(max_length=5, choices=CLASS_CHOICES, help_text="Class level of the student")

    # Guardian Information
    guardians_name = models.CharField(max_length=100, help_text="Guardian's full name")
    guardians_phone_number = models.CharField(max_length=15, help_text="Guardian's phone number")
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.admission_number})"
