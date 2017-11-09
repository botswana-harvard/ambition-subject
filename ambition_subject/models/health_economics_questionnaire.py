from .model_mixins import CrfModelMixin, MedicalExpensesMixin
from django.core.validators import MinValueValidator
from django.db import models
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_constants.choices import YES_NO


class MedicalExpensesManager(models.Manager):

    def get_by_natural_key(self, location_care, subject_identifier,
                           visit_schedule_name, schedule_name, visit_code):
        return self.get(
            location_care=location_care,
            health_economics_questionnaire__subject_visit__subject_identifier=subject_identifier,
            health_economics_questionnaire__subject_visit__visit_schedule_name=visit_schedule_name,
            health_economics_questionnaire__subject_visit__schedule_name=schedule_name,
            health_economics_questionnaire__subject_visit__visit_code=visit_code
        )


class HealthEconomicsQuestionnaire(MedicalExpensesMixin, CrfModelMixin):

    household_head = models.CharField(
        verbose_name='Are you head of the household?',
        max_length=5,
        choices=YES_NO)

    profession = models.CharField(
        verbose_name='What is your profession?',
        max_length=25,
        blank=True,
        null=True)

    education_years = models.IntegerField(
        verbose_name='How many years of education did you complete?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    education_certificate = models.CharField(
        verbose_name='What is your highest education certificate?',
        max_length=25,
        blank=True,
        null=True)

    elementary_school = models.CharField(
        verbose_name='Did you go to elementary school?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    elementary_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    secondary_school = models.CharField(
        verbose_name='Did you go to secondary school?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    secondary_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    higher_education = models.CharField(
        verbose_name='Did you go to higher education?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    higher_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_profession = models.CharField(
        verbose_name=('If you are not the head of household,'
                      ' what is the head of household profession?'),
        max_length=25,
        blank=True,
        null=True)

    head_education_years = models.IntegerField(
        verbose_name='How many years of education did '
        'head of houesehold complete?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_education_certificate = models.CharField(
        verbose_name='What is the head of household highest education '
        'certificate?',
        max_length=25,
        blank=True,
        null=True)

    head_elementary = models.CharField(
        verbose_name='Did the head of household go to elementary '
        'school?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    head_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_secondary = models.CharField(
        verbose_name='Did head of household go to secondary school?',
        max_length=5,
        blank=True,
        null=True,
        choices=YES_NO)

    head_secondary_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_higher_education = models.CharField(
        verbose_name='Did head of household go to higher education?',
        max_length=5,
        choices=YES_NO,
        blank=True,
        null=True)

    head_higher_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Health Economics Questionnaires'


class MedicalExpenses(BaseUuidModel, MedicalExpensesMixin):

    health_economics_questionnaire = models.ForeignKey(
        HealthEconomicsQuestionnaire, on_delete=models.CASCADE)

    objects = MedicalExpensesManager()

    def natural_key(self):
        return ((self.location_care,) + self.health_economics_questionnaire.natural_key())
    natural_key.dependencies = [
        'ambition_subject.healtheconomicsquestionnaire']

    class Meta:
        verbose_name_plural = 'Medical Expenses'
        unique_together = ('health_economics_questionnaire', 'location_care')
