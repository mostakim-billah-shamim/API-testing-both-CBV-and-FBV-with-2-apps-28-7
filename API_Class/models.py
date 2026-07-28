from django.db import models


class StudentModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    roll_number = models.IntegerField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class TeacherModel(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()

    def __str__(self):
        return self.name


# Create your models here.
