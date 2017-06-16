import re
from dateutil.relativedelta import relativedelta
from django.db.utils import IntegrityError
from model_mommy import mommy

from django.test import TestCase, tag

from edc_base.utils import get_utcnow
from edc_constants.constants import UUID_PATTERN, FEMALE

from ..forms import SubjectConsentForm
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


class TestSubjectConsentForm(TestCase):

    def setUp(self):
        self.subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening')

    @tag('f')
    def test_consent_age_not_match_screening_age(self):
        obj = mommy.prepare_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow,
            subject_screening=self.subject_screening,
            dob=(get_utcnow() - relativedelta(years=25)).date())
        data = obj.__dict__
        del data['subject_screening_id']
        data.update({'subject_screening': self.subject_screening.id})
        form = SubjectConsentForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    @tag('f')
    def test_consent_gender_not_match_screening_gender(self):
        obj = mommy.prepare_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow,
            subject_screening=self.subject_screening,
            dob=(get_utcnow() - relativedelta(years=40)).date(),
            gender=FEMALE)
        data = obj.__dict__
        del data['subject_screening_id']
        data.update({'subject_screening': self.subject_screening.id})
        form = SubjectConsentForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())
