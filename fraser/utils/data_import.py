import os
import csv
from datetime import datetime

from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from texts.models import Collection, Document

from django.utils import timezone
from django.conf import settings
from django.core.cache import cache
from django.db.models import Avg, Count, F, Max, Min, Sum, Q, Prefetch
from django.core.urlresolvers import reverse
from django.db import transaction


csvdata ={}
with open('fraser-radio-UMA-UDS-metadata.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    headers = reader.next()
    for row in reader:
        csvdata[row[1]] = {}
        csvdata[row[1]][headers[0]] = row[0]
        csvdata[row[1]][headers[6]] = row[6]
        csvdata[row[1]][headers[8]] = row[8]
        csvdata[row[1]][headers[12]] = row[12]

    notes = row[9]
    irn_url = row[11]

c = Collection.objects.get(id=1)

root = os.path.dirname(os.path.dirname(os.path.abspath('.')))
radio_talks = os.path.join(root, 'radio/UMA_Fraser_Radio_Talks')
files = os.listdir(radio_talks)

for f in files:
    fopen = open(os.path.join(radio_talks, f), "r")
    text = fopen.read()
    metadata, data = text.split("<!--end metadata-->")
    
    d = Document()
    d.body_text = data
    
    md = {}
    for line in metadata.split('\r\n'):
        if not line:
            continue
        if line[0] == '<':
            continue
        element = line.split(':', 1)
        md[element[0]] = element[1].strip()
    if md['Date'].startswith("c"):
        year = md['Date'][1:5]
        md['Date']="01/01/"+year
    elif not md['Date'].startswith('c'):
        x = md['Date']
        md['Date'] = datetime.strptime(x, '%d/%m/%Y').date()
        #:print md['Date']
    md['UDS'], garbage = f.rsplit('-',1)
    
        
    d.title = md['Title']
    d.description = md['Description']
    d.date_first = md['Date']
    d.collection = c
    d.collection_uma_id = csvdata[md['UDS']][headers[0]]
    d.uds_collection = md['UDS']
    d.format = md['Format']
    d.previous_control_number = csvdata[md['UDS']][headers[6]]
    d.extent_medium = csvdata[md['UDS']][headers[8]]
    d.irn = md['Collection URI']
    d.rights = csvdata[md['UDS']][headers[12]]
    text_path = settings.MEDIA_ROOT+"text/"
    d.text_file = os.path.join(text_path, f)
    d.image_file = "f"
    d.pdf_file = "f"
    d.save()




