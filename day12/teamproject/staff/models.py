from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    joined_date = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"