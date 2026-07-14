from django.db import models
from patients.models import Patient


class Visit(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="visits"
    )

    visit_date = models.DateField()

    diagnosis = models.TextField()

    treatment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.firstname} - {self.visit_date}"