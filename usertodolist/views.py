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
    if models.RegistrationModel.objects.filter(email=new_user.email):
        return HttpResponse("Diese Email ist schon vorhanden")
    else:
        if models.RegistrationModel.objects.filter(username=new_user.username):
            return HttpResponse("Dieser Username ist schon vergeben")
        else:
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
    post_username = request.POST.get("username")
    post_password = request.POST.get("password")
    if models.RegistrationModel.objects.filter(username=post_username, password=post_password):
        return render(request, "todolist/hometodo.html")
    else:
        return HttpResponse("Der Username oder das Passwort ist falsch!")



def hometodo(request):
    return render(request, "todolist/hometodo.html")

def todolist(request):
    context = {'id': '1'}
    context["todolist_form"] = forms.ToDoForm()
    return render(request, "todolist/todo.html", context)

def complete_todo(request):
    return HttpResponse("Gespeichert")