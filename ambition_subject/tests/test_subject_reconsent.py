from ambition_rando.tests.ambition_test_case_mixin import AmbitionTestCaseMixin
from django.core.exceptions import ValidationError, ObjectDoesNotExist,\
    MultipleObjectsReturned
from django.test import TestCase, tag
from edc_action_item.models.action_item import ActionItem
from edc_constants.constants import ABNORMAL, NORMAL, CLOSED
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy

from ..action_items import RECONSENT_ACTION


class TestReconsent(AmbitionTestCaseMixin, TestCase):

    def setUp(self):
        import_holidays()

    @tag('1')
    def test_abnormal(self):
        subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening',
            mental_status=ABNORMAL)
        subject_consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            screening_identifier=subject_screening.screening_identifier)
        try:
            mommy.make_recipe(
                'ambition_subject.subjectreconsent',
                subject_identifier=subject_consent.subject_identifier,
                identity=subject_consent.identity)
        except ValidationError:
            self.fail('ValidationError unexpectedly raised')

    @tag('1')
    def test_normal_raises(self):
        subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening',
            mental_status=NORMAL)
        subject_consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            screening_identifier=subject_screening.screening_identifier)
        self.assertRaises(
            ValidationError,
            mommy.make_recipe,
            'ambition_subject.subjectreconsent',
            subject_identifier=subject_consent.subject_identifier,
            identity=subject_consent.identity)

    @tag('1')
    def test_abnormal_creates_action(self):
        subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening',
            mental_status=ABNORMAL)
        subject_consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            screening_identifier=subject_screening.screening_identifier)
        try:
            ActionItem.objects.get(
                subject_identifier=subject_consent.subject_identifier,
                action_type__name=RECONSENT_ACTION)
        except ObjectDoesNotExist:
            self.fail('ActionItem unexpectedly does not exist')

    @tag('1')
    def test_abnormal_creates_only_one_action(self):
        subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening',
            mental_status=ABNORMAL)
        subject_consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            screening_identifier=subject_screening.screening_identifier)
        subject_consent.save()
        subject_consent.save()
        try:
            ActionItem.objects.get(
                subject_identifier=subject_consent.subject_identifier,
                action_type__name=RECONSENT_ACTION)
        except MultipleObjectsReturned:
            self.fail('More than one ActionItem unexpectedly exist')

    @tag('1')
    def test_abnormal_to_normal_deletes_new_action(self):
        subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening',
            mental_status=ABNORMAL)
        subject_consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            screening_identifier=subject_screening.screening_identifier)
        subject_screening.mental_status = NORMAL
        subject_screening.save()
        subject_consent.save()
        self.assertRaises(
            ObjectDoesNotExist,
            ActionItem.objects.get,
            subject_identifier=subject_consent.subject_identifier,
            action_type__name=RECONSENT_ACTION)

    @tag('1')
    def test_reconsent_updates_action_status(self):
        subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening',
            mental_status=ABNORMAL)
        subject_consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            screening_identifier=subject_screening.screening_identifier)
        subject_reconsent = mommy.make_recipe(
            'ambition_subject.subjectreconsent',
            subject_identifier=subject_consent.subject_identifier,
            identity=subject_consent.identity)
        action_item = ActionItem.objects.get(
            subject_identifier=subject_consent.subject_identifier,
            action_type__name=RECONSENT_ACTION)
        self.assertEqual(action_item.status, CLOSED)
