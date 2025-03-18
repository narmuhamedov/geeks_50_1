from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic
#create todo


class CreateTaskView(generic.CreateView):
    template_name = 'crud/create_task.html'
    form_class = forms.TaskForm
    success_url = "/task_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTaskView, self).form_valid(form=form)



# def create_task(request):
#     if request.method == 'POST':
#         form = forms.TaskForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#             #return HttpResponse('Вы успешно добавили задачу')
#     else:
#         form = forms.TaskForm()
#     return render(
#         request,
#         template_name='crud/create_task.html',
#         context={'form': form},
#     )

#read list/detail
class TaskListView(generic.ListView):
    template_name = 'crud/tasks_list.html'
    context_object_name = 'task'
    model = models.TodoList

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')




# def tasks_list(request):
#     if request.method == 'GET':
#         query = models.TodoList.objects.all().order_by('-id')
#         return render(
#             request,
#             template_name='crud/tasks_list.html',
#             context={'task': query},
#         )

class TaskDetailView(generic.DetailView):
    template_name = 'crud/task_detail.html'
    context_object_name = 'task_id'

    def get_object(self, *args, **kwargs):
        task_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoList, id=task_id)



# def task_detail(request, id):
#     if request.method == 'GET':
#         task_id = get_object_or_404(models.TodoList, id=id)
#         return render(
#             request,
#             template_name='crud/task_detail.html',
#             context={'task_id': task_id}
#         )


#Update
class UpdateTaskView(generic.UpdateView):
    template_name = 'crud/update_task.html'
    form_class = forms.TaskForm
    success_url = "/task_list/"

    def get_object(self, *args, **kwargs):
        task_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoList, id=task_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTaskView, self).form_valid(form=form)



# def update_task(request, id):
#     task_id = get_object_or_404(models.TodoList, id=id)
#     if request.method == 'POST':
#         form = forms.TaskForm(request.POST, instance=task_id)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#     else:
#         form = forms.TaskForm(instance=task_id)
#
#     return render(
#         request,
#         template_name='crud/update_task.html',
#         context={
#             'form': form,
#             'task_id': task_id
#         }
#     )


class DeleteTaskView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = "/task_list/"

    def get_object(self, *args, **kwargs):
        task_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoList, id=task_id)




# def delete_task(request, id):
#     task_id = get_object_or_404(models.TodoList, id=id)
#     task_id.delete()
#     return redirect('task_list')