import csv, json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.text import slugify

from .models import Document, Collection
from .forms import DocumentCorrectForm, DocumentCheckForm

class DocumentList(ListView):
    model = Document

class DocumentDetail(DetailView):
    model = Document

def tags(request):
    return render(request, 'texts/tag_index.html')
