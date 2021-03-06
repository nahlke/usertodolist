from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from usertodolist import forms
from usertodolist import models
from django.contrib import messages
from django.urls import reverse


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
        messages.warning(request, "Diese Email ist schon vorhanden")
        return user_registration(request)
    else:
        if models.RegistrationModel.objects.filter(username=new_user.username):
            messages.warning(request, "Dieser Username ist schon vergeben")
            return user_registration(request)
        else:
            if new_user.password == new_user.passwordrepeat:
                new_user.save()
                messages.success(request, "Registrierung erfolgreich")
                return signin(request)
            else:
                messages.warning(request, "Das Passwort stimmt nicht überein!")
                return user_registration(request)

# anzeigen der Anmeldeseite mit eingabefeldern
def signin(request):
    context = {'id': '1'}
    context["signin_form"] = forms.SignInForm()
    return render(request, "usersignin/signin.html", context)


# anmelden des users, wird geguckt ob user existiert und password übereinstimmt sonst fehlermeldung
def user_signin(request):
    models.SignInModel.objects.all().delete()
    post_username = request.POST.get("username")
    post_password = request.POST.get("password")
    new_user = models.SignInModel(username=post_username, password=post_password)
    if models.RegistrationModel.objects.filter(username=post_username, password=post_password):
        new_user.save()
        messages.success(request, "Angemeldet")
        return render(request, "todolist/hometodo.html")
    else:
        messages.warning(request, "Der Benutzername oder das Passwort ist falsch!")
        return signin(request)

# abmeldung des users
def signout(request):
    models.SignInModel.objects.all().delete()
    messages.success(request, "Abgemeldet")
    return homeregin(request)





# anzeigen der home seite von ToDo wenn man angemeldet ist
def hometodo(request):
    return render(request, "todolist/hometodo.html")


# anzeigen der Todo liste mit den eingetragenen sachen und den eingabefeldern
def todolist(request):
    user = models.SignInModel.objects.get()
    todos = models.ToDoListModel.objects.filter(username=user.username).order_by('status', 'title')
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
            messages.warning(request, "Dieser Titel ist schon vergeben!")
            return todolist(request)
        else:
            new_todo.save()
            messages.success(request, "Gespeichert")
            return todolist(request)
    else:
        messages.warning(request, "Der Benutzername ist falsch!")
        return todolist(request)

# löschen der liste
def deletelist(request):
    user = models.SignInModel.objects.get()
    models.ToDoListModel.objects.filter(username=user.username).delete()
    messages.info(request, "Die Liste wurde gelöscht!")
    return todolist(request)

# anzeigen der Todo liste mit den feldern zum verändern
def edit(request):
    user = models.SignInModel.objects.get()
    todos = models.ToDoListModel.objects.filter(username=user.username)
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
            messages.success(request, "Erfolgreich geändert")
            return todolist(request)
        else:
            messages.warning(request, "Der Benutzername ist falsch!")
            return edit(request)
    else:
        messages.warning(request, "Diesen Titel gibt es nicht!")
        return edit(request)

# anzeigen der Todo liste und dem eingabefeld zum auswählen welches gelöscht werden soll
def deletetodo(request):
    user = models.SignInModel.objects.get()
    todos = models.ToDoListModel.objects.filter(username=user.username)
    context = {'todos': todos}
    context["delete_form"] = forms.DelCompForm()
    return render(request, "todolist/delete.html", context)

# löschen des Todos aus der datenbank
def delete_save(request):
    post_title = request.POST.get("title")
    user = models.SignInModel.objects.get()
    if models.ToDoListModel.objects.filter(title=post_title, username=user.username):
        models.ToDoListModel.objects.filter(title=post_title, username=user.username).delete()
        messages.success(request, "ToDo gelöscht")
        return todolist(request)
    else:
        messages.warning(request, "Diesen Titel gibt es nicht!")
        return deletetodo(request)

# anzeigen der Todo liste mit den Todos die noch nicht erledigt sind und dem auswahlfeld
def complete(request):
    user = models.SignInModel.objects.get()
    todos = models.ToDoListModel.objects.filter(username=user.username)
    context = {'todos': todos}
    context["complete_form"] = forms.DelCompForm()
    return render(request, "todolist/complete.html", context)

# todo auf erledigt setzen und abspeichern
def complete_save(request):
    post_title = request.POST.get("title")
    user = models.SignInModel.objects.get()
    new_complete = models.ToDoListModel.objects.get(title=post_title, username=user.username)
    if models.ToDoListModel.objects.filter(title=post_title, username=user.username):
        if models.ToDoListModel.objects.filter(title=post_title, status=True, username=user.username):
            messages.warning(request, "Dieses ToDo ist schon erledigt!")
            return complete(request)
        else:
            new_complete.status = True
            new_complete.description = "Erledigt"
            new_complete.save()
            messages.success(request, "ToDo Erledigt")
            return todolist(request)
    else:
        messages.info(request, "Diesen Titel gibt es nicht!")
        return complete(request)