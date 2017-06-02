from edc_search.model_mixins import SearchSlugModelMixin as BaseSearchSlugModelMixin


class SearchSlugModelMixin(BaseSearchSlugModelMixin):

    def get_slugs(self):
        slugs = super().get_slugs()
        return slugs + [self.subject_identifier]

    class Meta:
        abstract = True
