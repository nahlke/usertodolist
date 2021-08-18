from requests import request
from usertodolist.models import RegistrationModel


class RegistrationForm(request):
    model = RegistrationModel
