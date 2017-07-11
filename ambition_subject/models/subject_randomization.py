from django.db import models
from django.core.validators import RegexValidator

from django_crypto_fields.fields import EncryptedCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel


class SubjectRandomizationManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(
            subject_identifier=subject_identifier,)


class SubjectRandomization(BaseUuidModel):

    study_site = models.CharField(
        verbose_name='Site',
        max_length=15)

    sid = models.IntegerField(
        verbose_name='SID',
        unique=True)

    rx = EncryptedCharField(
        verbose_name="Treatment Assignment")

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=16)

    randomization_datetime = models.DateTimeField(
        verbose_name='Randomization Datetime')

    initials = EncryptedCharField(
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}$',
            message=('Ensure initials consist of letters '
                     'only in upper case, no spaces.'))])

    objects = SubjectRandomizationManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,)

    def __str__(self):
        return f'{self.subject_identifier} {self.rx} {self.study_site} {self.sid}'

    class Meta():
        app_label = 'ambition_subject'
