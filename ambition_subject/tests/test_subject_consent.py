from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from model_mommy import mommy

from django.test import TestCase, tag

from edc_base.utils import get_utcnow

from ..models import SubjectConsent, Enrollment, Appointment


@tag('consent')
class TestSubjectConsent(TestCase):

    def test_cannot_create_consent_without_screening(self):
        """Test adding a consent without Subject screening first raises an
           Exception.
        """
        try:
            mommy.make_recipe(
                'ambition_subject.subject_consent',
                consent_datetime=get_utcnow,
            )
            self.fail('Exception not raised')
        except (IntegrityError, ValidationError):
            pass

    def test_allocated_subject_identifier(self):
        """Test consent successfully allocates subject identifier on save"""

        screening = mommy.make_recipe('ambition_subject.subject_screening')
        options = {
            'subject_screening_reference': screening.reference,
            'consent_datetime': get_utcnow, }
        mommy.make_recipe('ambition_subject.subject_consent', **options)
        RegisteredSubject = django_apps.get_app_config('edc_registration').model
        rs = RegisteredSubject.objects.all()[0]
        try:
            SubjectConsent.objects.get(subject_identifier=rs.subject_identifier)
        except SubjectConsent.DoesNotExist:
            self.fail('SubjectConsent.DoesNotExist unexpectedly raised')

    def test_consent_successfully_finds_subject_screening(self):
        """Test querying of subject consent with subject screening identifier"""

        screening = mommy.make_recipe('ambition_subject.subject_screening')
        mommy.make_recipe(
            'ambition_subject.subject_consent',
            consent_datetime=get_utcnow,
            subject_screening_reference=screening.reference)
        try:
            SubjectConsent.objects.get(subject_screening_reference=screening.reference)
        except SubjectConsent.DoesNotExist:
            self.fail('SubjectConsent.DoesNotExist unexpectedly raised')

    def test_enrollment_successfully_created(self):
        screening = mommy.make_recipe('ambition_subject.subject_screening')
        mommy.make_recipe(
            'ambition_subject.subject_consent',
            consent_datetime=get_utcnow,
            subject_screening_reference=screening.reference)
        enrollment = Enrollment.objects.all()
        self.assertTrue(enrollment[0].is_eligible)
        self.assertEqual(enrollment.count(), 1)
