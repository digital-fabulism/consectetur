from datetime import date
from django.contrib import admin

from .models import Collection, Document

class DecadeListFilter(admin.SimpleListFilter):
    title = 'decade delivered'
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return (
            ('50s', 'in the fifties'),
            ('60s', 'in the sixties'),
            ('70s', 'in the seventies'),
            ('80s', 'in the eighties'),
            ('90s', 'in the nineties'),
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
   list_display = ('title','get_year', 'description') 
   list_filter = (DecadeListFilter,)

admin.site.register(Collection)
admin.site.register(Document, DocumentAdmin)
