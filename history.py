import json
import xml.etree.ElementTree as ET
e = xml.etree.ElementTree.parse('transcripts.xml').getroot()
e = ET.parse('transcripts.xml').getroot()
pwd
cd pmtranscripts/data/
e = ET.parse('transcripts.xml').getroot()
e.findall(transcript)
e.findall('transcript')
for t in e.findall(transcript):
    t
for t in e.findall('transcript'):
    t
for t in e.findall('transcript'):
    print t
for t in e.findall('transcript'):
    print t['uri']
for t in e.findall('uri'):
    print t
for t in e.findall('uri'):
    print t
e.findall('transcript')
for t in e.findall('uri'):
    print t
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
pmtranscripts_meta = {}
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        print u.split('-')
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        print u.text.split('-')
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        print u.text.split('-')[1]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        print u.text.split('-')(1)
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        print u.text.split('-').1
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        print u.text.split('-')[0]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        print u.text.split('-')[1]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        url, id = u.text.split('-')
        print id
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        url = u.text.split('-')
        print url[1]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        url = u.text.split('-')
        print url
print url
print url[1]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        url = u.text.split('-')
        print url[1]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        url = u.text.split('-')
        for x,y in url:
            print y
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        url = u.text.split('-')
        for x in url:
            print y
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        url = u.text.split('-')
        for x in url:
            print x
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        url = u.text.split(1,'-')
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        print u.text
        url = u.text.split('-',1)
        print url
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-',1)
        print url
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-',1)
        print url[1]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-',1)
        for item in url:
            print item
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        print url[1]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        print url[0]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        print url[0]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        if len(u)>1:
     url = u.text.split('-')
     pmtranscripts_meta[url[1]] = url[0]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        if len(u)>1:
            url = u.text.split('-')
            pmtranscripts_meta[url[1]] = url[0]
pmtranscripts_meta
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        if len(u)>1:
            url = u.text.split('-')
            print url[1]
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        if len(u)>1:
            url = u.text.split('-')
            print url
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        if len(u)>1:
            print u url = u.text.split('-')
            print url
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        if len(u)>1:
            print u; url = u.text.split('-')
            print url
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        if len(u)>1:
            print u;
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        if len(url)>1:
            pmtranscripts_meta[url[1]]=url[0]
pmtranscripts_meta
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        if len(url)>1:
            pmtranscripts_meta[url[1]]=u
pmtranscripts_meta
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        if len(url)>1:
            pmtranscripts_meta[url[1]]=u.text
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        if len(url)>1:
            pmtranscripts_meta[url[1]]=u.text
pmtranscripts_meta
pmtranscripts_meta={}
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        if len(url)>1:
            pmtranscripts_meta[url[1]]=u.text
pmtranscripts_meta={}
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        if len(url)>1:
            pmtranscripts_meta[url[1]]=u.text
pmtranscripts_meta
history
pmtranscripts_meta={}
for t in e.findall('transcript'):
    for u in t.findall('uri'):
        url = u.text.split('-')
        if len(url)>1:
            pmtranscripts_meta[url[1]]={'base_url':u.text}
pmtranscripts_meta
for ts in pmtranscripts_meta:
    wget t ats['base_url']
     Grant of œ 7,000. had been given by the Commonweagth
     towards the Festival of Arts which is to be held in Adelaid
     in 1960. The Prime Minister said that in so doing
     the Commonweagth recognised the contribution the Festival
     would make in focussing attention on Australian cugtural
     achievements. Canberra,
     22nd October, 1959.]]>
            </content>
        </transcript>
    </transcripts>
for ts in pmtranscripts_meta:
    wget t ats['base_url']
     Grant of œ 7,000. had been given by the Commonweagth
     towards the Festival of Arts which is to be held in Adelaid
     in 1960. The Prime Minister said that in so doing
     the Commonweagth recognised the contribution the Festival
     would make in focussing attention on Australian cugtural
     achievements. Canberra,
     22nd October, 1959.]]>
            </content>
        </transcript>
    </transcripts>
for ts
for ts in pmtranscripts_meta:
    wget http://pmtranscripts.dpmc.gov.au/query?transcript=123   ts['base_url']
for ts in pmtranscripts_meta:
    print ts.key()
for ts in pmtranscripts_meta:
    print ts
for ts_key in pmtranscripts_meta:
    xml = wget 'http://pmtranscripts.dpmc.gov.au/query?transcript=%s' % ts_key
    pmtranscripts_meta[ts] = {'xml':xml}
for ts_key in pmtranscripts_meta:
    print 'http://pmtranscripts.dpmc.gov.au/query?transcript=%s' % ts_key
for ts_key in pmtranscripts_meta:
    response = urllib2.urlopen('http://pmtranscripts.dpmc.gov.au/query?transcript=%s' % ts_key)
    pmtranscripts_meta[ts] = {'xml':response.read()}
import urllib2
for ts_key in pmtranscripts_meta:
    response = urllib2.urlopen('http://pmtranscripts.dpmc.gov.au/query?transcript=%s' % ts_key)
    pmtranscripts_meta[ts] = {'xml':response.read()}
pmtranscripts_meta
for ts_key in pmtranscripts_meta:
    response = urllib2.urlopen('http://pmtranscripts.dpmc.gov.au/query?transcript=123')
    xml = response.read()
   print xml
for ts_key in pmtranscripts_meta:
    response = urllib2.urlopen('http://pmtranscripts.dpmc.gov.au/query?transcript=123')
    xml = response.read()
       print xml
for ts_key in pmtranscripts_meta:
    response = urllib2.urlopen('http://pmtranscripts.dpmc.gov.au/query?transcript=123')
    xml = response.read()
    print xml
response = urllib2.urlopen('http://pmtranscripts.dpmc.gov.au/query?transcript=123')
    xml = response.read()
    print xml
response = urllib2.urlopen('http://pmtranscripts.dpmc.gov.au/query?transcript=123')
    xml = response.read()
    print xml
response = urllib2.urlopen('http://pmtranscripts.dpmc.gov.au/query?transcript=123')
    xml = response.read()
    print xml
response = urllib2.urlopen('http://pmtranscripts.dpmc.gov.au/query?transcript=123')
         xml = response.read()
         print xml
%cpaste
%cpaste
%cpaste
import xmltodict
import xmldict
%cpaste
%cpaste
pmtranscripts_meta
import django
from ../fraser/texts/models.py import Document
from fraser.texts.models.py import Document
pwd
cd ../
from fraser.texts.models.py import Document
%history -f history.py
