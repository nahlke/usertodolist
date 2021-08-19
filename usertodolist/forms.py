from requests import request
from django.forms import ModelForm
from usertodolist.models import RegistrationModel, SigninModel, ToDoListModel


class RegistrationForm(ModelForm):
    class Meta:
        model = RegistrationModel
        fields = ["email", "username", "password", "passwordrepeat"]

class SigninForm(ModelForm):
    class Meta:
        model = SigninModel
        fields = ["username", "password"]

class ToDoForm(ModelForm):
    class Meta:
        model = ToDoListModel
        fields = ["title", "description", "status"]
