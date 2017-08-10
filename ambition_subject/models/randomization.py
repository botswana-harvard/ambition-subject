from edc_base.model_mixins import ListModelMixin
from edc_base.model_mixins import BaseUuidModel


class RandomizationItem (ListModelMixin, BaseUuidModel):

    class Meta:
        unique_together = ('display_index', 'name', 'field_name')
