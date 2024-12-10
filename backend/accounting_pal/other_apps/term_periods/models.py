# models.py
from django.db import models

class TermPeriod(models.Model):
    TERM_CHOICES = [
        ('Term 1', 'Term 1'),
        ('Term 2', 'Term 2'),
        ('Term 3', 'Term 3'),
    ]

    term_name = models.CharField(
        max_length=20,
        choices=TERM_CHOICES,
        help_text="Name of the term (e.g., Term 1, Term 2, Term 3)"
    )
    start_date = models.DateField(help_text="Start date of the term")
    end_date = models.DateField(help_text="End date of the term")
    year = models.PositiveIntegerField(help_text="Academic year associated with the term (e.g., 2024)")
    fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="The fee amount for each student for the term"
    )

    def __str__(self):
        return f"{self.term_name} {self.year} ({self.start_date} - {self.end_date})"
