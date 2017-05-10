from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO
from edc_constants.constants import YES, NO

from ..choices import REGIMEN
from ..constants import (N1, A2, AMS_N3, AMS_A4, SINGLE_DOSE,
                         CONTROL, THREE_DOSES, TWO_DOSES)

from .model_mixins import CrfModelMixin


class SubjectRandomization(CrfModelMixin):

    hospital_admission_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Date of hospital admission')

    abnormal_mental_status = models.CharField(
        choices=YES_NO,
        max_length=5,
        help_text='Abnormal mental status is GCS<15')

    on_arvs = models.CharField(
        choices=YES_NO,
        max_length=5)

    arv_start_date = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='If yes, ARV start date:')

    rando_category = models.CharField(
        editable=False,
        max_length=6)

    regimen = models.CharField(
        editable=False,
        max_length=15)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.rando_category, self.regimen = self.assign_randomization_category()
        super().save(*args, **kwargs)

    def assign_randomization_category(self):
        category = None
        regimen = None
        if self.on_arvs == YES:
            if self.abnormal_mental_status == YES:
                category = AMS_A4
                regimen = CONTROL
            if self.abnormal_mental_status == NO:
                category = A2
                regimen = TWO_DOSES
        if self.on_arvs == NO:
            if self.abnormal_mental_status == NO:
                category = N1
                regimen = SINGLE_DOSE
            if self.abnormal_mental_status == YES:
                category = AMS_N3
                regimen = THREE_DOSES
        return category, regimen

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
