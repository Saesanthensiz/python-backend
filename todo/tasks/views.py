from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tasks_list(request, *arrs, **kwargs):
    return render(request, 'tasks/task_list.html',{})
def work_list(request, *arrs, **kwargs):
    return render(request, 'tasks/work_list.html',{})