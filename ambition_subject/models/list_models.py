from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class AEClassification(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class Antibiotic(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class Day14Medication(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class MeningitisSymptom(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class MissedVisitReason(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class Medication(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class Neurological(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class SignificantNewDiagnosis(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class Symptom(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class OtherDrug(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'ambition_subject'


class RandomizationItem (ListModelMixin, BaseUuidModel):

    class Meta:
        app_label = 'ambition_subject'
        unique_together = ('display_index', 'name', 'field_name')
