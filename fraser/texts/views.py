from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Document, Collection

class DocumentList(ListView):
    model = Document

class DocumentDetail(DetailView):
    model = Document

class DocumentUpdate(UpdateView):
    model = Document

def electorate_talk_list(request):
    talks = Document.objects.filter(description="Electorate radio talk")
    return render(request, 'texts/electorate_list.html', {'talks': talks})

def press_statement_list(request):
    talks = Document.objects.filter(description="Press statement")
    return render(request, 'texts/press_statement_list.html', {'talks': talks})
