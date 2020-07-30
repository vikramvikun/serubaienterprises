from django.db import models
from django.contrib.auth.models import User

class index_table(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    img = models.ImageField(upload_to="media")
    description = models.TextField()

    def __str__(self):
        return str(self.name)
    
class services_table(models.Model):
    service_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media")
    description = models.TextField()

    def __str__(self):
        return str(self.service_name)

class works_table(models.Model):
    work_name = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    owner = models.CharField(max_length=30)
    description = models.TextField()
    img =models.ImageField(upload_to="media")

    def __str__(self):
        return str(self.work_name)

class contact_table(models.Model):
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    Address = models.TextField()

    def __str__(self):
        return str(self.email)

class subservice(models.Model):
    service_name = models.CharField(max_length=100)
    subservice_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media")
    description = models.TextField()

    def __str__(self):
        return str(self.subservice_name)

class works_done(models.Model):
    work_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="media")

    def __str__(self):
        return str(self.work_name)