from django.db import models

class RegistrationModel(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=18)
    passwordrepeat = models.CharField(max_length=18)

class ToDoListModel(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    status = models.BooleanField(null=True)

