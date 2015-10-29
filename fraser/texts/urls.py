from django.conf.urls import url

from .views import DocumentCheckList, DocumentCorrectList, DocumentCheck, DocumentCorrect, DocumentUpdate, DocumentDetail, DocumentList, electorate_talk_list, press_statement_list, archive_index, revert_document, finalize_document, TagDetailList, tags, document_concordance, timeline_json_output, timeline_json_output_1974

urlpatterns = [
    #url(r'^$', DocumentList.as_view(), name='archive_index'),
    url(r'^$', archive_index, name='archive_index'),
    url(r'^all_archives/$', archive_index, name='archive_index'),
    url(r'^timeline_js/$', timeline_json_output, name='timeline_js'),
    url(r'^timeline_js_1974/$', timeline_json_output_1974, name='timeline_js_1974'),
    url(r'^electorates/$', electorate_talk_list, name='electorates'),
    url(r'^press_statements/$', press_statement_list, name='press_statements'),
    url(r'^for_correction/$', DocumentCorrectList.as_view(), name='for_correction'),
    url(r'^for_checking/$', DocumentCheckList.as_view(), name='for_checking'),
    url(r'^tags/', tags, name='tags'), 
    url(r'^tag/(?P<slug>[-\w]+)/$', TagDetailList.as_view(), name='tag'),    
    url(r'^(?P<slug>[-\w]+)/$', DocumentDetail.as_view(), name='doc_detail'),
    url(r'^(?P<slug>[-\w]+)/conc/(?P<tag>[-\w]+)$', document_concordance, name='doc_concordance'),
    url(r'^(?P<slug>[-\w]+)/update/$', DocumentUpdate.as_view(), name='doc_update'),
    url(r'^(?P<slug>[-\w]+)/revert/$', revert_document, name='doc_revert'),
    url(r'^(?P<slug>[-\w]+)/finalized/$', finalize_document, name='doc_finalize'),
    url(r'^(?P<slug>[-\w]+)/correct/$', DocumentCorrect.as_view(), name='doc_correct'),
    url(r'^(?P<slug>[-\w]+)/check/$', DocumentCheck.as_view(), name='doc_check'),
]
