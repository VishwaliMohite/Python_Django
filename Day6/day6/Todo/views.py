from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'Todo/todo_list.html',{'todos':todos})

def todo_create(request):
   if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
   else:
        form = TodoForm()
   return render(request, 'Todo/todo_create.html',{'form':form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo,pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect('todo_list')
    return render(request, 'Todo/todo_delete.html',{'todo':todo})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'Todo/todo_create.html', {'form': form})
