from django import forms
from django.forms import ModelForm
from usertodolist.models import RegistrationModel, ToDoListModel


class RegistrationForm(ModelForm):
    class Meta:
        model = RegistrationModel
        fields = ["email", "username", "password", "passwordrepeat"]

class SigninForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    password = forms.CharField(label='password', max_length=30)

class ToDoForm(ModelForm):
    class Meta:
        model = ToDoListModel
        fields = ["title", "description", "status"]
