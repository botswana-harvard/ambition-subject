import re
from django.db.utils import IntegrityError
from model_mommy import mommy

from django.test import TestCase, tag

from edc_base.utils import get_utcnow
from edc_constants.constants import UUID_PATTERN

from ..models import SubjectConsent, Enrollment
from edc_registration.models import RegisteredSubject


class TestSubjectConsent(TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening')

    def test_cannot_create_consent_without_screening(self):
        """Test adding a consent without Subject screening first raises an
           Exception.
        """
        self.assertRaises(IntegrityError, mommy.make_recipe,
                          'ambition_subject.subjectconsent',
                          consent_datetime=get_utcnow)

    def test_allocated_subject_identifier(self):
        """Test consent successfully allocates subject identifier on
        save.
        """
        options = {
            'subject_screening': self.subject_screening,
            'consent_datetime': get_utcnow, }
        mommy.make_recipe('ambition_subject.subjectconsent', **options)
        self.assertFalse(
            re.match(
                UUID_PATTERN,
                SubjectConsent.objects.all()[0].subject_identifier))

    def test_consent_creates_registered_subject(self):
        options = {
            'subject_screening': self.subject_screening,
            'consent_datetime': get_utcnow, }
        self.assertEquals(RegisteredSubject.objects.all().count(), 0)
        mommy.make_recipe('ambition_subject.subjectconsent', **options)
        self.assertEquals(RegisteredSubject.objects.all().count(), 1)

    def test_enrollment_created_on_consent(self):
        subject_consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow,
            subject_screening=self.subject_screening)

        try:
            Enrollment.objects.get(
                consent_identifier=subject_consent.consent_identifier)
        except Enrollment.DoesNotExist:
            self.fail('Enrollment.DoesNotExist: was unexpectedly raised.')
