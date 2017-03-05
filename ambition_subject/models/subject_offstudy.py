from edc_base.model_mixins import HistoricalRecords, BaseUuidModel
from edc_offstudy.model_mixins import OffstudyModelMixin, OffstudyModelManager


class SubjectOffstudy(OffstudyModelMixin, BaseUuidModel):

    """A model completed by the user that completed when the
    subject is taken off-study.
    """

    objects = OffstudyModelManager()

    history = HistoricalRecords()

    class Meta:
        app_label = "ambition_subject"
        verbose_name = "Subject Off Study"
        verbose_name_plural = "Subject Off Study"
