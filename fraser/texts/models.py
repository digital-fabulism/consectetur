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
    
    bigrams = jsonfield.JSONField()
    trigrams = jsonfield.JSONField()
    body_text_marked = models.CharField(max_length=21000, blank=True) 
    concordances = jsonfield.JSONField()

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
            self.bigrams = self.get_bigrams()
            self.trigrams = self.get_trigrams()
            # TODO: remove recursion, make get/set:
            #self.mark_body_text()
            #self.tag_me()
            
            self.format = "Corrected OCR text"
        super(Document, self).save()

    def return_timeline_json(self):
        #This is ugly, fix it (TODO)
        url = ''.join(['http://fraser.digitalfabulists.org', self.ge
        ngrams = []                                                 
        for tg in self.trigrams:
            for key, val in tg.iteritems():
                ngrams.append(key)
        for bg in self.bigrams:
            for key, val in bg.iteritems():
                ngrams.append(key)
        
        ngram_str = ', '.join(ngrams)
        doc_dict = {  
                    "start_date": {
                        "year":  self.date_first.year,
                        "month": self.date_first.month,
                        "day":   self.date_first.day,
                        "hour":         "",
                        "minute":       "",
                        "second":       "",
                        "millisecond":  "",
                        "format":       ""
                    },
                     "end_date": {
                        "year":         "",
                        "month":        "",
                        "day":          "",
                        "hour":         "",
                        "minute":       "",
                        "second":       "",
                        "millisecond":  "",
                        "format":       ""
                    },
                    "media": {
                        "caption":      "",
                        "credit":       "",
                        "url":          "",
                        "thumbnail":    ""
                    },
                    "text": {
                        "headline": self.title,
                        "text": ngram_str    
                    }
            }
        return doc_dict

    def get_year(self):
        return self.date_first.year

    def ngrammer(self, gramsize=2, threshold=2):
        
        # return the ngram and count of appearances in speech
        def ngram_frequency_distribution(seq):
            tally = defaultdict(list)
            ngram_freq_dist = []
            for i,item in enumerate(seq):
                tally[item].append(i)
            for ngram, linenumber in tally.items():
                if len(linenumber) > threshold:
                    ngram_freq_dist.append({ngram: len(linenumber)})
            return ngram_freq_dist 
                  
        '''
            Get text all in lowercase, tokenize text,
            remove punctutation, get gramsize ngrams
        '''
        text = self.body_text.lower()
        text = nltk.word_tokenize(text)
        text = [token for token in text if token.isalnum()]
        shingles = ngrams(text, gramsize)
        
        '''
            remove ignored words, get frequency distribution
        '''
        shingles_list = ngram_frequency_distribution(shingles)
        ignored_words = nltk.corpus.stopwords.words('english')
        ignored_words.extend(nltk.corpus.stopwords.words('justext_english'))
        ignored_words = list(set(ignored_words))
        shingle_list_w_frequency = []
        
        for ngram_dist in shingles_list:
            for words, count in ngram_dist.iteritems():
                if not any(word in ignored_words for word in words):
                    ngram = " ".join(words)
                    shingle_list_w_frequency.append({ngram: count})
        
        # return them, sorted by most frequent
        return sorted(shingle_list_w_frequency, reverse = True)

    def get_bigrams(self):
        bigrams = json.dumps(self.ngrammer(gramsize=2))
        return bigrams
    
    def set_bigrams(self):
        self.bigrams = self.get_bigrams()
        self.save()

    def get_trigrams(self):
        trigrams = json.dumps(self.ngrammer(gramsize=3))
        return trigrams

    def set_trigrams(self):
        self.trigrams = self.get_trigrams()
        self.save()

    def repl(self, ngram=None):
        for match in re.findall(ngram, self.body_text_marked, re.I):
            repl = '<span class="%s">%s</span>' % ( slugify(match), match)
            self.body_text_marked = re.sub(match, repl, self.body_text_marked)
            break

    def mark_body_text(self):
        self.body_text_marked = self.body_text.replace("\r\n\r\n","<p>")
        self.body_text_marked = self.body_text_marked.replace("\r\n"," ")
        if len(self.trigrams) > 0:
            for ngram_freq in self.trigrams:
                for ngram, count in ngram_freq.iteritems():
                    self.repl(ngram=ngram)
            self.save()
        if len(self.bigrams) > 0:
            for ngram_freq in self.bigrams:
                for ngram, count in ngram_freq.iteritems():
                    self.repl(ngram=ngram)
            self.save()
 
    def tag_me(self):
        for gramsize in (2,3):
            for ngram in self.ngrammer(gramsize=gramsize):
                for shingle, count in ngram.iteritems():
                    self.tags.add(shingle)
        self.save()

    def get_conc(self, tag=None):
        for ngram in self.trigrams + self.bigrams:
            for text, count in ngram.items():
                if slugify(text) == tag:
                    return self.concordances[text]

    def get_concordances(self):
        '''
        Prepare the text 
            - remove line breaks, but retain paragraphs
            - lowercase everything
        '''
        prepared_text = self.body_text.replace("\r\n\r\n","&*****&")
        prepared_text = prepared_text.replace("\r\n"," ")
        prepared_text = prepared_text.replace("&*****&", "\r\n")       
        prepared_text = prepared_text.lower()

        concordance_collection = {}       
        ngram_concordance_list = []

        # check the text has information in it
        if not self.bigrams:
            self.set_bigrams()
        if not self.trigrams:
            self.set_trigrams()
        if len(self.bigrams) == 0 and len(self.trigrams) == 0:
            return json.dumps(concordance_collection)

        # create the concordances
        for ngram in self.trigrams + self.bigrams:
            for text, count in ngram.items():
                cl = [(q.start(), q.end()) for q in re.finditer(text, prepared_text)]
                for start, end in cl:
                    concline = prepared_text[start-30:start], text, prepared_text[end:end+30]
                    ngram_concordance_list.append(concline)
                concordance_collection[text] = ngram_concordance_list
                ngram_concordance_list = []
        return json.dumps(concordance_collection)

    def set_concordance(self):
        self.concordances = self.get_concordances()
        self.save()
