import csv, json

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.text import slugify

from .models import Document

class DocumentList(ListView):
    model = Document

class DocumentDetail(DetailView):
    model = Document

def find_blanks(request):
    blanks = Document.objects.filter( Q(title__isnull=True) | Q(prime_minister__isnull=True) | Q(period_of_service__isnull=True) | Q(release_date__isnull=True) | Q(document_url__isnull=True) | Q(content__isnull=True))
    return render(request, 'texts/blanks.html', {'blanks': blanks})

def tags(request):
    return render(request, 'texts/tag_index.html')
