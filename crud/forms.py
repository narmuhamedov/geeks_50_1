from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.TodoList
        fields = '__all__'