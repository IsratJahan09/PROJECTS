from django.shortcuts import render , redirect
from .models import todo
# Create your views here.
def index(request):
    if request.method == 'POST':
        text = request.POST.get("text").strip()
        if text:
            todo.objects.create(text=text)
        return redirect('/')
    todos = todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def deleteto(request, id):
    todo.objects.get(id=id).delete()
    return redirect('/')

def about(request):
    return render(request, 'about.html')