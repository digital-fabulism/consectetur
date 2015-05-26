from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Document, Collection
from .forms import DocumentCorrectForm, DocumentCheckForm

def archive_index(request):
    electorate = Document.objects.filter(description="Electorate radio talk")
    press_statements = Document.objects.filter(description="Press statement")
    other = Document.objects.exclude(description="Electorate radio talk").exclude(description="Press statement")
    return render(request, 'texts/archive_list.html', {'electorate': electorate, 'press_statements':press_statements, 'other':other})
    

class DocumentList(ListView):
    model = Document

class DocumentCheckList(ListView):
    model = Document
    queryset = Document.objects.filter(correction_check=True)
    template_name_suffix = "_checklist"

class DocumentCorrectList(ListView):
    model = Document
    queryset = Document.objects.filter(correction_needed = True)    
    template_name_suffix = "_correctlist"

class DocumentDetail(DetailView):
    model = Document

class DocumentUpdate(UpdateView):
    model = Document
    fields = ['title', 'description', 'date_first', 'date_last', 'collection', 'collection_uma_id', 'uds_number', 'format', 'previous_control_number', 'extent_medium', 'notes', 'irn', 'rights', 'text_file', 'image_file', 'pdf_file'] 

class DocumentCheck(UpdateView):
    model = Document
    template_name_suffix = '_check'
    form_class = DocumentCheckForm

class DocumentCorrect(UpdateView):
    model = Document
    template_name_suffix = '_correct'
    form_class = DocumentCorrectForm

def revert_document(request, slug=None):
    document = Document.objects.get(slug=slug)
    document.correction_needed = True
    document.correction_check = False
    document.correction_complete = False
    document.save()
    return redirect(document)

def finalize_document(request, slug=None):
    document = Document.objects.get(slug=slug)
    document.correction_needed = False
    document.correction_check = False
    document.correction_complete = True
    document.save()
    return redirect(document)
    

def electorate_talk_list(request):
    talks = Document.objects.filter(description="Electorate radio talk")
    return render(request, 'texts/electorate_list.html', {'talks': talks})

def press_statement_list(request):
    talks = Document.objects.filter(description="Press statement")
    return render(request, 'texts/press_statement_list.html', {'talks': talks})
