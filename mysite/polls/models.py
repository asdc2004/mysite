# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField('Author')
    publisher = models.Foreignkey('publisher', on_delete=models.CASCADE)
    publisher_date = models.DateTimeField()

    def __str__(selfself):
        return  self.title

    class Author(models.Model):
        name = models.CharField(max_length=50)
        salutation = models.CharField(max_length=100)
        email = models.EmailField()

        def __str__(self):
            return  self.name

    class Publisher(models.Model):
        name = models.CharField(max_length=50)
        address = models.CharField(max_length=100)
        website=models.URLField()

        def __str__(self):
            return  self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.Foreignkey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
