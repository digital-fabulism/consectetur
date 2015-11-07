from datetime import date
from django.contrib import admin

from .models import Document

class PDFFilter(admin.SimpleListFilter):
    title = 'pdfs'
    parameter_name='pdf'

    def lookups(self, request, model_admin):
        return (
                ('none', 'No PDF'),
                ('some', 'Has PDF'),
               )

    def queryset(self, request, queryset):
        if self.value() == 'none':
            return queryset.filter(pdf_file='')
        if self.value() == 'some':
            return queryset.exclude(pdf_file='')

class DocumentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Details', {'fields': ('naa_transcript_id', 'title', 'prime_minister'), }),
        ('Archival details', {'fields': (('period_of_service', 'release_date'), ('release_type', 'document_url'), 'subjects')}),
        ('Summary', {'fields': ('content',)}),
    )
    list_display = ('prime_minister','title','release_date') 

admin.site.register(Document, DocumentAdmin)
