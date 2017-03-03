from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_metadata.model_mixins.metadata_models import CrfModelMixin


class CrfMetadata(CrfModelMixin, BaseUuidModel):

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition'
