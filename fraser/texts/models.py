from django.db import models
from django.utils.text import slugify

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
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    date_first = models.DateField(blank=True,null=True)
    date_last = models.DateField(blank=True, null=True)
    collection = models.ForeignKey(Collection)
    collection_uma_id = models.CharField(max_length=4)
    uds_number = models.CharField(max_length=14)
    format = models.CharField(max_length=25)
    previous_control_number = models.CharField(max_length=15)
    extent_medium = models.CharField(max_length=20)
    notes = models.CharField(max_length=1500)
    irn = models.URLField()
    rights = models.CharField(max_length=500)
    slug = models.SlugField(max_length=14)
    
    text_file = models.FileField(upload_to='text/', max_length=100)
    image_file = models.ImageField(upload_to='image/', max_length=100)
    pdf_file = models.FileField(upload_to='pdf/', max_length=100)


    def id_number(self):
        return "%s.%s" %(self.collection, self.collection_id)
    
    def __unicode__(self):
        return "%s, %s" %(self.title, self.id_number())

    def save(self):    
        uma_id = "%s.%s" %(self.collection, self.collection_id)
        self.slug = slugify(uma_id)
        super(Document, self).save()

