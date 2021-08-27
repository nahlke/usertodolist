from django import forms
from django.forms import ModelForm
from usertodolist.models import RegistrationModel, ToDoListModel, SignInModel


#form die für die Registrierung benötigt wird
class RegistrationForm(ModelForm):
    password = forms.CharField(label='Passwort', widget=forms.PasswordInput)
    passwordrepeat = forms.CharField(label='Passwort wiederholen', widget=forms.PasswordInput)
    username = forms.CharField(label='Benutzername')
    class Meta:
        model = RegistrationModel
        fields = ["email", "username", "password", "passwordrepeat"]

#form die für die Anmeldung benötigt wird
class SignInForm(ModelForm):
    username = forms.CharField(label='Benutzername')
    password = forms.CharField(label='Passwort', widget=forms.PasswordInput)
    class Meta:
        model = SignInModel
        fields = ["username", "password"]

#form die für die todo liste benötigt wird
class ToDoForm(ModelForm):
    title = forms.CharField(label='Titel')
    description = forms.CharField(label='Beschreibung')
    username = forms.CharField(label='Benutzername')
    class Meta:
        model = ToDoListModel
        fields = ["title", "description", "username"]

#form die für das bearbeiten der todo liste benötigt wird
class EditForm(ModelForm):
    newtitle = forms.CharField(label='Neuer Titel')
    title = forms.CharField(label='Titel')
    description = forms.CharField(label='Neue Beschreibung')
    username = forms.CharField(label='Dein Benutzername')
    class Meta:
        model = ToDoListModel
        fields = ["title", "description", "username"]

#form die zum löschen und erledigen benötigt wird
class DelCompForm(ModelForm):
    title = forms.CharField(label='Titel')
    class Meta:
        model = ToDoListModel
        fields = ["title"]

