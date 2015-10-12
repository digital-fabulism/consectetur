from django import forms

from .models import Document

class DocModelForm(forms.ModelForm):
    body_text = forms.CharField(widget=forms.Textarea)
    body_text_marked = forms.CharField(widget=forms.Textarea)

    class Meta:
	    fields = ['title', 'description', 'date_first', 'date_last', 'collection', 'collection_uma_id', 'uds_number', 'format', 'previous_control_number', 'extent_medium', 'notes', 'irn', 'rights', 'slug', 'body_text', 'text_file', 'image_file', 'pdf_file', 'body_text_marked']        
	    model = Document
    
class DocumentCorrectForm(forms.ModelForm):
    body_text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'cols': 10, 'rows': 25}))
   
    def save(self, commit=True):
        instance = super(DocumentCorrectForm, self).save(commit=False)
        instance.correction_needed = False
        instance.correction_check = True
        instance.correction_complete = False
        #instance.
        if commit:
            instance.save()
        return super(DocumentCorrectForm, self).save() 

    class Meta:
        model = Document
        fields = ['body_text'] 

class DocumentCheckForm(forms.ModelForm):
    body_text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'cols': 10, 'rows': 25}))
   
    class Meta:
        model = Document
        fields = ['body_text'] 
