from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email_id = models.EmailField()
    date_of_birth = models.DateField()
    enrolled_in = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name


# Create your models here.
