from datetime import date
from django.contrib import admin

from .models import Collection, Document
from .forms import DocModelForm

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

class DocumentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Details', {'fields': (('title', 'date_first', 'date_last'), 'notes')}),
        ('Archival details', {'fields': (('collection', 'collection_uma_id'), ('uds_number', 'previous_control_number'), 'irn')}),
        ('Summary', {'fields': (('extent_medium', 'format', 'rights'), 'body_text')}),
        ('Files', {'fields': ('text_file', 'image_file', 'pdf_file')}),
    )
    list_display = ('title','get_year', 'description') 
    list_filter = (DecadeListFilter, 'description',)
    form = DocModelForm

admin.site.register(Collection)
admin.site.register(Document, DocumentAdmin)
