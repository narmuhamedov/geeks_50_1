from django.urls import path
from . import views

urlpatterns = [
    path('create_task/', views.CreateTaskView.as_view(), name='create_task'),
    path('task_list/', views.TaskListView.as_view(), name='task_list'),
    path('task_list/<int:id>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('task_list/<int:id>/update/', views.UpdateTaskView.as_view(), name='task_update'),
    path('task_list/<int:id>/delete/', views.DeleteTaskView.as_view(), name='task_delete'),
]