from django.db import models



class PatientModel(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  gender = models.CharField(max_length=20)
  phone_number = models.CharField(max_length=15, unique=True)
  email = models.EmailField(unique=True)
  address = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name


class DoctorModel(models.Model):
  name = models.CharField(max_length=100)
  specialization = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=15, unique=True)
  email = models.EmailField(unique=True)
  consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
  available_days = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Dr. {self.name} ({self.specialization})"
