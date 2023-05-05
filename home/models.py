from django.contrib.auth.models import User
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=35)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=250,)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.questions.title

