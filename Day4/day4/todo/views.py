from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_create(request):
  if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
  else:
        form = TodoForm()
  return render(request, 'todo/todo_form.html',{'form':form})
        
            
            
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html',{'todos':todos})

