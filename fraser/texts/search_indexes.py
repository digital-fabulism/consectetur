from haystack import indexes
from texts.models import Document


class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    collection_uma_id = indexes.CharField(model_attr='collection_uma_id')
    date_first = indexes.DateTimeField(model_attr='first_date')

    def get_model(self):
        return Document

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
