from django.shortcuts import render

from polls.models import Question, Choice
from django.urls import  reverse
from django.http import HttpResponseRedirect
from polls.forms import  NameForm

def name(request, data = None):
    form = NameForm(data)
    return render(request, 'polls/name.html', {'form': form})

# Create your views here.

from django.views.generic.base import  TemplateView
from django.views.generic import ListView
from  django.views.generic import DetailView
from books.models import  Book, Author, Publisher

#TemplateView
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list']=['Book','Author','Publisher']
        return  context

    class BookList(ListView):
        model=Book

    class AuthorList(ListView):
        model = Author
    class PublisherList(ListView):
        model = Publisher

    class BookDetail(DetailView):
        model=Book

    class AuthorDetail(DetailView):
        model = Author

    class PublisherDetail(DetailView):
        model=Publisher