from django.conf.urls import url

from .views import DocumentDetail, DocumentList, tags, find_blanks

urlpatterns = [
    url(r'^$', DocumentList.as_view(), name='archive_index'),
    url(r'^blanks/$', find_blanks, name='blanks'),
    url(r'^tags/', tags, name='tags'), 
    url(r'^doc/(?P<slug>[-w]+)/$', DocumentDetail.as_view(), name='doc_detail'),
    #url(r'^tag/(?P<slug>[-\w]+)/$', TagDetailList.as_view(), name='tag'),    
]
