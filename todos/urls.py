from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.todo_form,name='todo_update'),
    path('register/',views.todo_form,name='todo_register'),
    path('list/',views.todo_list,name='todo_list'),
    path('delete/<int:id>/',views.todo_delete,name='todo_delete'),
    

   


]