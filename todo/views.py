from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect,get_object_or_404,render


# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def markAsDone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def markAsUnDone(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.POST:
        new_task = request.POST['task']
        task.task = new_task
        task.save()
    else:
        context={
            "task":task
        }
        return render(request,'edit.html',context)
    return redirect('home')

def deleteTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')
