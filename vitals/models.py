from django.db import models
from patients.models import Patient


class Vital(models.Model):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="vitals"
    )

    visit_date = models.DateField()

    height = models.FloatField()

    weight = models.FloatField()

    bmi = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.firstname} - {self.visit_date}"