from django import forms
from django.apps import apps as django_apps
from ambition_validators import MicrobiologyFormValidator

from ..models import Microbiology

from .form_mixins import SubjectModelFormMixin
from pprint import pprint


class MicrobiologyForm(SubjectModelFormMixin):

    form_validator_cls = MicrobiologyFormValidator

    subject_consent_model = 'ambition_subject.subjectconsent'

    def clean(self):
        """check sample date
        """
        cleaned_data = super().clean()
        model_cls = django_apps.get_model(self.subject_consent_model)
        pprint(cleaned_data)
        subject_identifier = cleaned_data.get(
            'subject_visit').subject_identifier
        consent = model_cls.objects.get(subject_identifier=subject_identifier)
        consent_date = consent.consent_datetime.date()
        blood_taken_date = cleaned_data.get('blood_taken_date')
        if blood_taken_date:
            day_blood_taken = self.cleaned_data.get('day_blood_taken')
            study_days = (blood_taken_date - consent_date).days
            if day_blood_taken and day_blood_taken > study_days:
                raise forms.ValidationError({
                    'day_blood_taken': f'Randomization date is '
                    f'{consent_date}, blood sample study day should '
                    f'be {study_days} days or less.'})
        return cleaned_data

    class Meta:
        model = Microbiology
        fields = '__all__'
