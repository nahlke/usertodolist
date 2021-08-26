from django.shortcuts import render
from django.http import HttpResponse
from usertodolist import forms
from usertodolist import models


# Anzeigen der Seite wenn keine url eingegeben(Homeseite)
def homeregin(request):
    return render(request, "usersignin/homeregin.html")


# anzeigen der Registrierungsseite mit eingabefeldern
def user_registration(request):
    context = {'id': '1'}
    context["registration_form"] = forms.RegistrationForm()
    return render(request, "usersignin/registration.html", context)


# erstellen und abspeichern des Users wenn alles richtig ist, sonst fehlermedlung
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


# anzeigen der Anmeldeseite mit eingabefeldern
def signin(request):
    context = {'id': '1'}
    context["signin_form"] = forms.SignInForm()
    return render(request, "usersignin/signin.html", context)


# anmelden des users, wird geguckt ob user existiert und password übereinstimmt sonst fehlermeldung
def user_signin(request):
    post_username = request.POST.get("username")
    post_password = request.POST.get("password")
    new_user = models.SignInModel(username=post_username, password=post_password)
    if models.RegistrationModel.objects.filter(username=post_username, password=post_password):
        new_user.save()
        return render(request, "todolist/hometodo.html")
    else:
        return HttpResponse("Der Benutzername oder das Passwort ist falsch!")

def signout(request):
    models.SignInModel.objects.all().delete()
    return homeregin(request)





# anzeigen der home seite von ToDo wenn man angemeldet ist
def hometodo(request):
    return render(request, "todolist/hometodo.html")


# anzeigen der Todo liste mit den eingetragenen sachen und den eingabefeldern
def todolist(request):
    todos = models.ToDoListModel.objects.filter(username="Nils")
    context = {'todos': todos}
    context["todolist_form"] = forms.ToDoForm()
    return render(request, "todolist/todo.html", context)


# abspeichern der neuen todo und zurück gehen zu todo seite
def complete_todo(request):
    post_title = request.POST.get("title")
    post_description = request.POST.get("description")
    post_username = request.POST.get("username")
    new_todo = models.ToDoListModel(title=post_title, description=post_description, username=post_username)
    if models.SignInModel.objects.filter(username=post_username):
        if models.ToDoListModel.objects.filter(title=post_title, username=post_username):
            return HttpResponse("Dieser Titel ist schon vergeben.")
        else:
            new_todo.save()
            return todolist(request)
    else:
        return HttpResponse("Der Benutzername ist falsch!")

# löschen der liste
def deletelist(request):
    models.ToDoListModel.objects.filter(username="Nils").delete()
    return todolist(request)

# anzeigen der Todo liste mit den feldern zum verändern
def edit(request):
    todos = models.ToDoListModel.objects.filter(username="Nils")
    context = {'todos': todos}
    context["edit_form"] = forms.EditForm()
    return render(request, "todolist/edit.html", context)

# abspeichern des bearbeiteten todos
def edit_save(request):
    post_newtitle = request.POST.get("newtitle")
    post_title = request.POST.get("title")
    post_description = request.POST.get("description")
    post_username = request.POST.get("username")
    if models.ToDoListModel.objects.filter(title=post_title):
        if models.SignInModel.objects.filter(username=post_username):
            new_todo = models.ToDoListModel.objects.get(title=post_title, username=post_username)
            new_todo.title = post_newtitle
            new_todo.description = post_description
            new_todo.username = post_username
            new_todo.save()
            return todolist(request)
        else:
            return HttpResponse("Der Benutzername ist falsch!")
    else:
        return HttpResponse("Diesen Titel gibt es nicht!")


def deletetodo(request):
    todos = models.ToDoListModel.objects.filter(username="Nils")
    context = {'todos': todos}
    context["delete_form"] = forms.DeleteForm()
    return render(request, "todolist/delete.html", context)

def delete_save(request):
    post_title = request.POST.get("title")
    if models.ToDoListModel.objects.filter(title=post_title, username="Nils"):
        models.ToDoListModel.objects.filter(title=post_title).delete()
        return todolist(request)
    else:
        return HttpResponse("Diesen Titel gibt es nicht!")

def complete(request):
    todos = models.ToDoListModel.objects.filter(username="Nils")
    context = {'todos': todos}
    context["complete_form"] = forms.CompleteForm()
    return render(request, "todolist/complete.html", context)

def complete_save(request):
    post_title = request.POST.get("title")
    new_complete = models.ToDoListModel.objects.get(title=post_title, username="Nils")
    if models.ToDoListModel.objects.filter(title=post_title, username="Nils"):
        if models.ToDoListModel.objects.filter(title=post_title, status=True, username="Nils"):
            return HttpResponse("Dieses ToDo ist schon erledigt!")
        else:
            new_complete.status = True
            new_complete.description = "Erledigt"
            new_complete.save()
            return todolist(request)
    else:
        return HttpResponse("Diesen Titel gibt es nicht!")