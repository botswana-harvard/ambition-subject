from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class AEClassification (ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = "ambition_subject"
