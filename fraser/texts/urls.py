from django.conf.urls import url

from .views import DocumentUpdate, DocumentDetail, DocumentList, electorate_talk_list, press_statement_list

urlpatterns = [
    url(r'^$', DocumentList.as_view(), name='index'),
    url(r'^electorates/$', electorate_talk_list, name='electorates'),
    url(r'^press_statements/$', press_statement_list, name='press_statements'),
    url(r'^(?P<slug>[-\w]+)/$', DocumentDetail.as_view(), name='doc_detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', DocumentUpdate.as_view(), name='doc_update'),
]