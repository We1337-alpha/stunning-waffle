from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo item added!")
            return redirect('todo')
    else:
        form = TodoForm()

    context = {
        "forms": form, 
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', context)

def remove(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    item.delete()
    messages.success(request, "Item removed!")
    return redirect('todo')