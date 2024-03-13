from django.db import models

class Company(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    #headcount <- the number of employees in that company
    
    def __str__(self):
        return self.name + " @ " + self.location

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.first_name) + " " +  str(self.last_name) + " at " + str(self.company)