from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import TodoForm
from .models import Todo

# Create your views here.

def todo_list(request):
    todos = { 'todo_list' : Todo.objects.all() }
    return render(request,"todos/todo_list.html", todos)

def todo_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = TodoForm ()
        else:
            todo = Todo.objects.get(pk=id)
            form = TodoForm(instance=todo)
        return render(request,"todos/todo_form.html",{'form':form})
    else:
        if id==0:
            form = TodoForm (request.POST)
        else:
            todo = Todo.objects.get(pk=id)
            form = TodoForm(request.POST,instance = todo)
        if form.is_valid():
            
            form.save()
            print(request.user.id)
        return redirect('/todos/list')

def todo_delete(request,id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return redirect('/todos/list')


#def list_todo_items(request):
 #   todo_list = { 'todo_list' : Todo.objects.all() }
  #  return render(request,'todos/todo_list.html', todo_list)

#def insert_todo_item(request:HttpRequest):
 #   current_user = request.user
  #  todo = Todo(content = request.POST['content'],user_id = current_user.id)
   # todo.save()
   # return redirect('/todos/list/')

#def delete_todo_item(request,todo_id):
 #   todo_to_delete = Todo.objects.get(id=todo_id)
  #  todo_to_delete.delete()
   # return redirect('/todos/list/')
