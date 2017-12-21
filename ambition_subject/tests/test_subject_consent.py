import re

from ambition_prn.models import OnSchedule
from ambition_rando.import_randomization_list import import_randomization_list
from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import UUID_PATTERN
from edc_registration.models import RegisteredSubject
from model_mommy import mommy

from ..models import SubjectConsent
from django.core.exceptions import ObjectDoesNotExist


class TestSubjectConsent(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        self.subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening')

    def test_allocated_subject_identifier(self):
        """Test consent successfully allocates subject identifier on
        save.
        """
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        mommy.make_recipe('ambition_subject.subjectconsent', **options)
        self.assertFalse(
            re.match(
                UUID_PATTERN,
                SubjectConsent.objects.all()[0].subject_identifier))

    def test_consent_creates_registered_subject(self):
        options = {
            'screening_identifier': self.subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        self.assertEquals(RegisteredSubject.objects.all().count(), 0)
        mommy.make_recipe('ambition_subject.subjectconsent', **options)
        self.assertEquals(RegisteredSubject.objects.all().count(), 1)

    def test_onschedule_created_on_consent(self):
        subject_consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow,
            screening_identifier=self.subject_screening.screening_identifier)

        try:
            OnSchedule.objects.get(
                consent_identifier=subject_consent.consent_identifier)
        except ObjectDoesNotExist:
            self.fail('ObjectDoesNotExist was unexpectedly raised.')

#     def test_consent_assigns_rando_arm(self):
#         options = {
#             'subject_screening': self.subject_screening,
#             'consent_datetime': get_utcnow, }
#         consent = mommy.make_recipe(
#             'ambition_subject.subjectconsent', **options)
#         randomized = SubjectRandomization.objects.get(
#             subject_identifier=consent.subject_identifier)
#         self.assertEqual(
#             randomized.rx,
#             RandomizationItem.objects.get(name=randomized.sid).field_name)
#
#         subject_screening = mommy.make_recipe(
#             'ambition_screening.subjectscreening')
#         options = {
#             'subject_screening': subject_screening,
#             'consent_datetime': get_utcnow, }
#         consent = mommy.make_recipe(
#             'ambition_subject.subjectconsent', **options)
#
#         randomized2 = SubjectRandomization.objects.get(
#             subject_identifier=consent.subject_identifier)
#         self.assertNotEqual(
#             randomized.sid,
#             RandomizationItem.objects.get(name=randomized2.sid).name)
#
#     def test_rando_follows_all_sequences(self):
#         rando_list = RandomizationItem.objects.all()
#         for rando in rando_list:
#             self.subject_screening = mommy.make_recipe(
#                 'ambition_screening.subjectscreening')
#             options = {
#                 'subject_screening': self.subject_screening,
#                 'consent_datetime': get_utcnow, }
#             mommy.make_recipe(
#                 'ambition_subject.subjectconsent', **options)
#
#         for rando in rando_list:
#             self.assertEqual(
# int(rando.name), SubjectRandomization.objects.get(sid=rando.name).sid)
