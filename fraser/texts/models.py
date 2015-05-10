from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager

class Collection(models.Model):
    title = models.CharField(max_length=100)
    uri = models.URLField()
    ref_number = models.CharField(max_length=9)
    historical_context = models.CharField(max_length=1500)
    rights = models.CharField(max_length=500)
    slug = models.SlugField(max_length=9)

    def __unicode__(self):
        return "%s, %s" %(self.title, self.ref_number)

    def save(self):
        self.slug = slugify(self.ref_number)
        super(Collection, self).save()

class Document(models.Model):
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=67)
    date_first = models.DateField(blank=True,null=True)
    date_last = models.DateField(blank=True, null=True)
    collection = models.ForeignKey(Collection)
    collection_uma_id = models.CharField("Collection UMA ID", max_length=14)
    uds_number = models.CharField("UDS Number", max_length=14)
    format = models.CharField(max_length=25)
    previous_control_number = models.CharField(max_length=15)
    extent_medium = models.CharField(max_length=25)
    notes = models.CharField(max_length=1500, blank=True)
    irn = models.URLField("IRN")
    rights = models.CharField(max_length=500, blank=True)

    correction_needed = models.BooleanField(default=True)
    correction_check = models.BooleanField(default=False)
    correction_complete = models.BooleanField(default=False)

    body_text = models.CharField(max_length=20000) 
    text_file = models.FileField(upload_to='text/', max_length=100, blank=True, null=True)
    image_file = models.ImageField(upload_to='image/', max_length=100, blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdf/', max_length=100, blank=True, null=True)
    
    slug = models.SlugField(max_length=100)
    tags = TaggableManager()
    
    class Meta:
        ordering =['date_first']
    
    def get_absolute_url(self):
        return reverse('doc_detail', args=[self.slug])
    
    def id_number(self):
        return "%s.%s" %(self.collection, self.collection_uma_id)
    
    def __unicode__(self):
        return "%s,%s" %(self.title, self.id_number())

    def save(self):    
        self.slug = slugify(self.id_number())
        if correction_complete:
            self.format = "Corrected OCR text"
        super(Document, self).save()

    def get_year(self):
        return self.date_first.year
