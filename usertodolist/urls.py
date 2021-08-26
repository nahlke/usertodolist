from django.urls import path
from usertodolist import views

urlpatterns = [
    path('', views.homeregin, name='homeregin'),
    path('registration', views.user_registration, name='registration'),
    path('signin', views.signin, name='signin'),
    path('usersignin', views.user_signin, name='usersignin'),
    path('user_create', views.user_create, name='user_create'),
    path('usersignin', views.user_signin, name='usersignin'),
    path('hometodo', views.hometodo, name='hometodo'),
    path('todolist', views.todolist, name='todolist'),
    path('completetodo', views.complete_todo, name='completetodo'),
    path('deletelist', views.deletelist, name='deletelist'),
    path('signout', views.signout, name='signout'),
    path('edit', views.edit, name='edit'),
    path('editsave', views.edit_save, name='editsave'),
    path('deletetodo', views.deletetodo, name='deletetodo'),
    path('deletesave', views.delete_save, name='deletesave'),
    path('complete', views.complete, name='complete'),
    path('completesave', views.complete_save, name='completesave'),
]