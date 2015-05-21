import nltk
from nltk.util import ngrams
from collections import defaultdict

from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.conf import settings

from taggit.managers import TaggableManager

nltk.data.path.append(settings.NLTK_DATA)

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

    def freq(self):
        docs = c.document_set.all()


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
    
    #bigrams = models.CharField(max_length=
    #trigrams =
    slug = models.SlugField(max_length=100)
    tags = TaggableManager(blank=True)
    
    class Meta:
        ordering =['date_first']
    
    def get_absolute_url(self):
        return reverse('doc_detail', args=[self.slug])
    
    def id_number(self):
        return "%s.%s" %(self.collection, self.collection_uma_id)
    
    def __unicode__(self):
        return "%s, %s" %(self.title, self.id_number())

    def save(self):    
        self.slug = slugify(self.id_number())
        if self.correction_complete:
            self.format = "Corrected OCR text"
        super(Document, self).save()

    def get_year(self):
        return self.date_first.year

    def ngrammer(self, gramsize=2, threshold=2):
        text = self.body_text.lower()

        # get ngrams of gramsize    
        if type(text) != list:
            text = nltk.word_tokenize(text)
        text = [token for token in text if token.isalnum()]
        # get ngrams of gramsize    
        raw_grams = ngrams(text, gramsize)
        
        # a subdefinition to get duplicate lists in a list
        def list_duplicates(seq):
            tally = defaultdict(list)
            for i,item in enumerate(seq):
                tally[item].append(i)
                # return to us the index and the ngram itself:
            return ((len(locs),key) for key,locs in tally.items() 
                   if len(locs) > threshold)

        # use our duplication detector to find duplicates
        dupes = list_duplicates(raw_grams)
        ignored_words = nltk.corpus.stopwords.words('english')
        # add more stopwords
        ignored_words.extend(nltk.corpus.stopwords.words('justext_english'))
        # deduplicate the stopwords :)
        ignored_words = list(set(ignored_words))
        good_words = []
        for count, words in dupes:
            if any(word not in ignored_words for word in words):
               good_words.append(gram)
        # return them, sorted by most frequent
        return sorted(good_words, reverse = True)
