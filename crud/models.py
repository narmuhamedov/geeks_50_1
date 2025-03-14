from django.db import models
from films.models import Films

class TodoList(models.Model):
    STATUS = (
        ('✅', '✅'),
        ('❌', '❌')
    )
    title = models.CharField(max_length=100)
    choice_films = models.ForeignKey(Films, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='❌')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



