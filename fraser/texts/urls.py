from django.conf.urls import url

from .views import DocumentCorrect, DocumentUpdate, DocumentDetail, DocumentList, electorate_talk_list, press_statement_list, archive_index

urlpatterns = [
    #url(r'^$', DocumentList.as_view(), name='archive_index'),
    url(r'^$', archive_index, name='archive_index'),
    url(r'^all_archives/$', archive_index, name='archive_index'),
    url(r'^electorates/$', electorate_talk_list, name='electorates'),
    url(r'^press_statements/$', press_statement_list, name='press_statements'),
    url(r'^(?P<slug>[-\w]+)/$', DocumentDetail.as_view(), name='doc_detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', DocumentUpdate.as_view(), name='doc_update'),
    url(r'^(?P<slug>[-\w]+)/correct/$', DocumentCorrect.as_view(), name='doc_correct'),
]
