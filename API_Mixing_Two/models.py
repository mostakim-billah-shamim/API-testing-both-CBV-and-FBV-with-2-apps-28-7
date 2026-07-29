from django.db import models



class AppointmentModel(models.Model):
  patient_name = models.CharField(max_length=100)
  doctor_name = models.CharField(max_length=100)
  appointment_date = models.DateField()
  appointment_time = models.TimeField()
  status = models.CharField(
      max_length=20, default='Pending'
  ) 
  symptoms = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.patient_name} - {self.appointment_date}'



class MedicalRecordModel(models.Model):
  patient_name = models.CharField(max_length=100)
  diagnosis = models.CharField(max_length=200)
  prescribed_medications = models.TextField()
  lab_tests = models.TextField(blank=True, null=True)
  next_visit_date = models.DateField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'Record for {self.patient_name}'

# Create your models here.
