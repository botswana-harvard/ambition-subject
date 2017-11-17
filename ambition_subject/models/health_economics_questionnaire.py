from django.db import models
from django.db.models.deletion import PROTECT
from django.core.validators import MinValueValidator
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_constants.constants import NOT_APPLICABLE

from ..choices import YES_NO, LOCATION_CARE, CARE_PROVIDER, TRANSPORT
from ..validators import hm_validator
from .model_mixins import CrfModelMixin


class HealthEconomicsQuestionnaire2Manager(models.Manager):

    def get_by_natural_key(self, location_care, subject_identifier,
                           visit_schedule_name, schedule_name, visit_code):
        return self.get(
            location_care=location_care,
            health_economics_questionnaire__subject_visit__subject_identifier=subject_identifier,
            health_economics_questionnaire__subject_visit__visit_schedule_name=visit_schedule_name,
            health_economics_questionnaire__subject_visit__schedule_name=schedule_name,
            health_economics_questionnaire__subject_visit__visit_code=visit_code
        )


class HealthEconomicsQuestionnaire(CrfModelMixin):

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Health Economics Questionnaires'


class HealthEconomicsQuestionnaire2(BaseUuidModel):

    health_economics_questionnaire = models.ForeignKey(
        HealthEconomicsQuestionnaire, on_delete=PROTECT)

    location_care = models.CharField(
        verbose_name='If Yes, where did you receive treatment or care?',
        max_length=35,
        choices=LOCATION_CARE)

    location_care_other = OtherCharField()

    transport_form = models.CharField(
        verbose_name='Which form of transport did you take to reach '
        'there?',
        max_length=20,
        choices=TRANSPORT,
        default=NOT_APPLICABLE)

    transport_cost = models.DecimalField(
        verbose_name='How much did you spend on the transport (each way)?',
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)

    transport_duration = models.CharField(
        verbose_name='How long did it take you to reach there?',
        validators=[hm_validator],
        max_length=8,
        help_text='in hours:minutes',
        null=True,
        blank=True)

    care_provider = models.CharField(
        verbose_name='Who provided treatment or care during that visit?',
        max_length=35,
        choices=CARE_PROVIDER)

    care_provider_other = OtherCharField(
        verbose_name='If Other Specify:',
        max_length=25,
        blank=True,
        null=True)

    paid_treatment = models.CharField(
        verbose_name=(
            'Did you pay for the treatment '
            'you received during that visit'),
        max_length=15,
        choices=YES_NO)

    paid_treatment_amount = models.DecimalField(
        verbose_name=(
            'How much did you pay for this visit?'),
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)

    medication_bought = models.CharField(
        verbose_name='Did you buy other medication for relief?',
        max_length=15,
        choices=YES_NO)

    medication_payment = models.DecimalField(
        verbose_name='How much did you pay?',
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)

    other_place_visited = models.CharField(
        verbose_name='Before this, did you go to another place '
        'for the treatment of the present situation?',
        max_length=15,
        choices=YES_NO)

    objects = HealthEconomicsQuestionnaire2Manager()

    def natural_key(self):
        return ((self.location_care,) + self.health_economics_questionnaire.natural_key())
    natural_key.dependencies = [
        'ambition_subject.healtheconomicsquestionnaire']

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Health Economics Questionnaire Inlines'
        unique_together = ('health_economics_questionnaire', 'location_care')
