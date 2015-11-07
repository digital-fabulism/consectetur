from django.conf.urls import url

from .views import DocumentDetail, DocumentList, tags

urlpatterns = [
    url(r'^$', DocumentList.as_view(), name='archive_index'),
    url(r'^tags/', tags, name='tags'), 
    url(r'^tag/(?P<slug>[-\w]+)/$', TagDetailList.as_view(), name='tag'),    
]
