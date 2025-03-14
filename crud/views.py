from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.http import HttpResponse
#create todo
def create_task(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('task_list')
            #return HttpResponse('Вы успешно добавили задачу')
    else:
        form = forms.TaskForm()
    return render(
        request,
        template_name='crud/create_task.html',
        context={'form': form},
    )

#read list/detail
def tasks_list(request):
    if request.method == 'GET':
        query = models.TodoList.objects.all().order_by('-id')
        return render(
            request,
            template_name='crud/tasks_list.html',
            context={'task': query},
        )

def task_detail(request, id):
    if request.method == 'GET':
        task_id = get_object_or_404(models.TodoList, id=id)
        return render(
            request,
            template_name='crud/task_detail.html',
            context={'task_id': task_id}
        )


#Update
def update_task(request, id):
    task_id = get_object_or_404(models.TodoList, id=id)
    if request.method == 'POST':
        form = forms.TaskForm(request.POST, instance=task_id)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = forms.TaskForm(instance=task_id)

    return render(
        request,
        template_name='crud/update_task.html',
        context={
            'form': form,
            'task_id': task_id
        }
    )


def delete_task(request, id):
    task_id = get_object_or_404(models.TodoList, id=id)
    task_id.delete()
    return redirect('task_list')