from django.shortcuts import render
from django.http import HttpResponse
from usertodolist import forms
from usertodolist import models


def homeregin(request):
    return render(request, "usersignin/homeregin.html")

def user_registration(request):
    context = {'id':'1'}
    context["registration_form"] = forms.RegistrationForm()
    return render(request, "usersignin/registration.html", context)

def user_create(request):
    post_email = request.POST.get("email")
    post_username = request.POST.get("username")
    post_password = request.POST.get("password")
    post_passwordrepeat = request.POST.get("passwordrepeat")
    new_user = models.RegistrationModel(email=post_email, username=post_username, password=post_password,
                                        passwordrepeat=post_passwordrepeat)
    if new_user.password == new_user.passwordrepeat:
        new_user.save()
        return HttpResponse("Registrierung erfolgreich")
    else:
        return HttpResponse("Das Passwort stimmt nicht überein")

def signin(request):
    context = {'id': '1'}
    context["signin_form"] = forms.SigninForm()
    return render(request, "usersignin/signin.html", context)

def user_signin(request):
    # post_username = request.POST.get("username")
    # post_password = request.POST.get("password")
    # new_user = models.SigninModel(username=post_username, password=post_password)
    # if new_user.password:
    #    new_user.save()
    return render(request, "todolist/hometodo.html")
    # else:
    #    return HttpResponse("Der Username oder das Passwort ist falsch!")



def hometodo(request):
    return render(request, "todolist/hometodo.html")

def todolist(request):
    return render(request, "todolist/todo.html")