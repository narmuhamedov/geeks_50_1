from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title