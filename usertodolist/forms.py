from django import forms
from django.forms import ModelForm
from usertodolist.models import RegistrationModel, ToDoListModel


class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    passwordrepeat = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = RegistrationModel
        fields = ["email", "username", "password", "passwordrepeat"]

class SigninForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    password = forms.CharField(label='password', max_length=30, widget=forms.PasswordInput)

class ToDoForm(ModelForm):
    class Meta:
        model = ToDoListModel
        fields = ["title", "description"]
