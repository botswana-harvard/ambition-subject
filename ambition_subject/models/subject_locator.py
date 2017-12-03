from django.db import models
from django_crypto_fields.fields import EncryptedCharField
from edc_base.model_validators import CellNumber, TelephoneNumber
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_constants.constants import NOT_APPLICABLE
from edc_constants.choices import YES_NO_NA, YES_NO
from edc_consent.model_mixins import RequiresConsentMixin
from edc_locator.model_mixins import LocatorModelMixin


class SubjectLocator(LocatorModelMixin, RequiresConsentMixin, BaseUuidModel):
    """A model completed by the user to that captures participant
    locator information and permission to contact.
    """

    home_visit_permission = models.CharField(
        max_length=25,
        choices=YES_NO,
        verbose_name=("Has the participant given his/her permission for study"
                      "staff to make home visits for follow-up purposes?"))

    alt_contact_cell_number = EncryptedCharField(
        max_length=8,
        verbose_name="Cell number (alternate)",
        validators=[CellNumber, ],
        blank=True,
        null=True)

    has_alt_contact = models.CharField(
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        verbose_name=(
            'If we are unable to contact the person indicated above, '
            'is there another individual (including next of kin) with '
            'whom the study team can get in contact with?'))

    alt_contact_name = EncryptedCharField(
        max_length=35,
        verbose_name="Full Name of the responsible person",
        help_text="include first name and surname",
        blank=True,
        null=True)

    alt_contact_rel = EncryptedCharField(
        max_length=35,
        verbose_name="Relationship to participant",
        blank=True,
        null=True)

    alt_contact_cell = EncryptedCharField(
        max_length=8,
        verbose_name="Cell number",
        validators=[CellNumber, ],
        blank=True,
        null=True)

    other_alt_contact_cell = EncryptedCharField(
        max_length=8,
        verbose_name="Cell number (alternate)",
        validators=[CellNumber, ],
        blank=True,
        null=True)

    alt_contact_tel = EncryptedCharField(
        max_length=8,
        verbose_name="Telephone number",
        validators=[TelephoneNumber, ],
        help_text="",
        blank=True,
        null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.subject_identifier

    class Meta(RequiresConsentMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
