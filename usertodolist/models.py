from django.db import models


#models/tabellenfelder die fürs registrieren benötigt werden
class RegistrationModel(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=18)
    passwordrepeat = models.CharField(max_length=18)

#models/tabellenfelder die benötigt werden um zu wissen wer angemeldet ist
class SignInModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=18)

#models/tabellenfelder die für die todo liste benötigt werden
class ToDoListModel(models.Model):
    title = models.CharField(max_length=32, null=True)
    description = models.CharField(max_length=256, null=True)
    username = models.CharField(max_length=20)
    status = models.BooleanField(False, null=True)

