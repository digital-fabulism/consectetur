import nltk
from nltk.util import ngrams
from collections import defaultdict
import json
import re

from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.conf import settings

from taggit.managers import TaggableManager
import jsonfield

nltk.data.path.append(settings.NLTK_DATA)

class Document(models.Model):
    naa_transcript_id = models.CharField(max_length=8)
    title = models.CharField(max_length=140)
    prime_minister = models.CharField(max_length=30)
    period_of_service = models.CharField(max_length=20)
    release_date = models.DateField()
    release_type = models.CharField(max_length=30)
    document_url = models.URLField()
    subjects = models.CharField(max_length=400)
    content = models.CharField(max_length=50000)

    bigrams = jsonfield.JSONField()
    trigrams = jsonfield.JSONField()
    concordances = jsonfield.JSONField()

    slug = models.SlugField(max_length=100)
    tags = TaggableManager(blank=True)
    
    def get_absolute_url(self):
        return reverse('doc_detail', args=[self.slug])
    
    def __unicode__(self):
        return "%s" %(self.naa_transcript_id)

    def save(self):    
        self.slug = slugify(self.naa_transcript_id)
        #self.bigrams = self.get_bigrams()
        #self.trigrams = self.get_trigrams()
        super(Document, self).save()
