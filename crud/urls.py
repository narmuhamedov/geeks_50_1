from django.urls import path
from . import views

urlpatterns = [
    path('create_task/', views.create_task, name='create_task'),
    path('task_list/', views.tasks_list, name='task_list'),
    path('task_list/<int:id>/', views.task_detail, name='task_detail'),
    path('task_list/<int:id>/update/', views.update_task, name='task_update'),
    path('task_list/<int:id>/delete/', views.delete_task, name='task_delete'),
]