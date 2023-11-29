from django.contrib import admin
from polls.models import Question, Choice
from  books.models import Book, Author, Publisher
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)

