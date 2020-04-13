from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TODO


# Create your views here.
def index(request):
    q = TODO.objects.all()
    return render(request, 'todo/index.html', {'LIST': q})


def addtodo(request):
    work = request.POST['work']
    q = TODO(text=work)
    q.save()
    return HttpResponseRedirect('/')


def delete(request, todo_id):
    q1 = TODO.objects.get(id=todo_id)
    q1.delete()

    return HttpResponseRedirect('/')
