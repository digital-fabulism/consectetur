from django import forms

from .models import Document

class DocModelForm(forms.ModelForm):
    body_text = forms.CharField(widget=forms.Textarea)

    class Meta:
	    fields = ['title', 'description', 'date_first', 'date_last', 'collection', 'collection_uma_id', 'uds_number', 'format', 'previous_control_number', 'extent_medium', 'notes', 'irn', 'rights', 'slug', 'body_text', 'text_file', 'image_file', 'pdf_file']        
	    model = Document
    
class DocumentCorrectForm(forms.ModelForm):
    body_text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'cols': 10, 'rows': 25}))
    
    class Meta:
        model = Document
        fields = ['body_text'] 
