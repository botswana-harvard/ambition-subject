from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class AEClassification(ListModelMixin, BaseUuidModel):

    pass


class Antibiotic(ListModelMixin, BaseUuidModel):

    pass


class AntibioticTreatment(ListModelMixin, BaseUuidModel):

    pass


class Day14Medication(ListModelMixin, BaseUuidModel):

    pass


class MeningitisSymptom(ListModelMixin, BaseUuidModel):

    pass


class MissedVisitReason(ListModelMixin, BaseUuidModel):

    pass


class Medication(ListModelMixin, BaseUuidModel):

    pass


class Neurological(ListModelMixin, BaseUuidModel):

    pass


class SignificantNewDiagnosis(ListModelMixin, BaseUuidModel):

    pass


class Symptom(ListModelMixin, BaseUuidModel):

    pass


class OtherDrug(ListModelMixin, BaseUuidModel):

    pass


class AbnormalResultsReason(ListModelMixin, BaseUuidModel):

    pass


class CXRType(ListModelMixin, BaseUuidModel):

    pass


class InfiltrateLocation(ListModelMixin, BaseUuidModel):

    pass
