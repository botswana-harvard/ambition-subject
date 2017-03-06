from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class AEClassification (ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = "ambition_subject"


class Neurological (ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = "ambition_subject"
        verbose_name = "Neurological"


class Symptoms (ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = "ambition_subject"
        verbose_name = "Symptoms"
