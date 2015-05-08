from django.conf.urls import include, url
from datetime import date
from django.contrib import admin
from django.shortcuts import render
import csv
from django.http import HttpResponse

from .models import Collection, Document
from .forms import DocModelForm

class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(MyModelAdmin, self).get_urls()
        my_urls = [
            url(r'^radio_csv/$', self.radio_talks_csv_export),
            url(r'^electoral_csv/$', self.electoral_csv_export),
            url(r'^press_csv/$', self.press_csv_export),
            url(r'^other_csv/$', self.other),
        ]
        return my_urls + urls

    def radio_talks_csv_export(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="radio_talks.csv"'

        talks = Document.objects.filter(description__contains="adio")

        writer = csv.writer(response)
        writer.writerow(['UMA', 'Title', 'Description'])
        
        for doc in talks:
            writer.writerow([doc.collection_uma_id, doc.title, doc.description])

        return response    

    def electoral_csv_export(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="electoral.csv"'

        talks = Document.objects.filter(description__contains="lectoral")

        writer = csv.writer(response)
        writer.writerow(['UMA', 'Title', 'Description'])
        
        for doc in talks:
            writer.writerow([doc.collection_uma_id, doc.title, doc.description])

        return response    
        
    def press_csv_export(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="press.csv"'

        talks = Document.objects.filter(description__contains="ress")

        writer = csv.writer(response)
        writer.writerow(['UMA', 'Title', 'Description'])
        
        for doc in talks:
            writer.writerow([doc.collection_uma_id, doc.title, doc.description])

        return response    

    def other(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="other.csv"'

        wtalks = Document.objects.filter(description__contains="eekly")
        stalks = Document.objects.filter(description__contains="tatement")
        writer = csv.writer(response)
        writer.writerow(['UMA', 'Title', 'Description'])
        
        for doc in wtalks:
            writer.writerow([doc.collection_uma_id, doc.title, doc.description])
        for doc in stalks:
            writer.writerow([doc.collection_uma_id, doc.title, doc.description])

        return response    
     

class DecadeListFilter(admin.SimpleListFilter):
    title = 'decade delivered'
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return (
            ('50s', 'The Fifties'),
            ('60s', 'The Sixties'),
            ('70s', 'The Seventies'),
            ('80s', 'The Eighties'),
            ('90s', 'The Nineties'),
        )

    def queryset(self, request, queryset):
          if self.value() == '50s':
            return queryset.filter(date_first__gte=date(1950, 1, 1),
                                    date_first__lte=date(1959, 12, 31))
          if self.value() == '60s':
            return queryset.filter(date_first__gte=date(1960, 1, 1),
                                    date_first__lte=date(1969, 12, 31))
          if self.value() == '70s':
            return queryset.filter(date_first__gte=date(1970, 1, 1),
                                    date_first__lte=date(1979, 12, 31))
          if self.value() == '80s':
            return queryset.filter(date_first__gte=date(1980, 1, 1),
                                    date_first__lte=date(1989, 12, 31))
          if self.value() == '90s':
            return queryset.filter(date_first__gte=date(1990, 1, 1),
                                    date_first__lte=date(1999, 12, 31))

#class DocumentAdmin(admin.ModelAdmin):
class DocumentAdmin(MyModelAdmin):
   list_display = ('title','get_year', 'description') 
   list_filter = (DecadeListFilter, 'description',)
   form = DocModelForm

admin.site.register(Collection)
admin.site.register(Document, DocumentAdmin)
