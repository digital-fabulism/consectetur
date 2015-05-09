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

