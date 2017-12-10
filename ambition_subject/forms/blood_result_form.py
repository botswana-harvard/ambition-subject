from django.apps import apps as django_apps
from django import forms
from edc_reportable import site_reportables

from ambition_validators import BloodResultFormValidator

from ..models import BloodResult
from .form_mixins import SubjectModelFormMixin
from pprint import pprint


class BloodResultForm(SubjectModelFormMixin, forms.ModelForm):

    form_validator_cls = BloodResultFormValidator

#     def clean(self):
#         cleaned_data = super().clean()
#         summary = []
#         subject_identifier = cleaned_data.get(
#             'subject_visit').subject_identifier
#         RegisteredSubject = django_apps.get_model(
#             'edc_registration.registeredsubject')
#         registered_subject = RegisteredSubject.objects.get(
#             subject_identifier=subject_identifier)
#
#         reportables = site_reportables.get('ambition')
#         gender = registered_subject.gender
#         if not gender:
#             raise ValueError(f'gender is unknown! See {repr(self)}')
#         dob = registered_subject.dob
#         if not dob:
#             raise ValueError(f'dob is unknown! See {repr(self)}')
#         subject_visit = cleaned_data.get('subject_visit')
#
#         for field, value in cleaned_data.items():
#             print(field, value)
#             grp = reportables.get(field)
#             if value and grp:
#                 grade = grp.get_grade(
#                     value, gender=gender, dob=dob, units='g/dL',
#                     report_datetime=subject_visit.report_datetime)
#                 if grade and grade.grade:
#                     summary.append(
#                         f'{field.title()} is reportable. Got {grade.description}.')
#         cleaned_data['summary'] = '\n'.join(summary)
#         return cleaned_data

    class Meta:
        model = BloodResult
        fields = '__all__'
