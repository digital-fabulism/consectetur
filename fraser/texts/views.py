from django.shortcuts import render
import csv
from django.http import HttpResponse

from texts.models import Document

# Create your views here.


def radio_talks_csv_export2():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="radio_talks.csv"'

    talks = Document.objects.filter(description__contains="adio")

    writer = csv.writer(response)
    writer.writerow(['UMA', 'Title', 'Description'])
    
    for doc in talks:
        writer.writerow([doc.collection_uma_id, doc.title, doc.description])

    return response    

def radio_talks_csv_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="radio_talks.csv"'

    talks = Document.objects.filter(description__contains="adio")

    writer = csv.writer(response)
    writer.writerow(['UMA', 'Title', 'Description'])
    
    for doc in talks:
        writer.writerow([doc.collection_uma_id, doc.title, doc.description])

    return response    
