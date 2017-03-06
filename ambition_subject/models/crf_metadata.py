from edc_base.model_mixins import BaseUuidModel
from edc_metadata.model_mixins.metadata_models import CrfModelMixin


class CrfMetadata(CrfModelMixin, BaseUuidModel):

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition'
