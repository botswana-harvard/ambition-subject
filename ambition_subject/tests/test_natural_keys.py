from django.test import TestCase, tag

from edc_sync.tests import SyncTestHelper


class TestNaturalKey(TestCase):

    sync_test_helper = SyncTestHelper()

    @tag('natural_key')
    def test_natural_key_attrs(self):
#         exclude_models = [
#             'ambition_subject.symptom', 'ambition_subject.significantnewdiagnosis',
#             'ambition_subject.aeclassification', 'ambition_subject.antibiotic',
#             'ambition_subject.antibiotictreatment', 'ambition_subject.day14medication',
#             'ambition_subject.meningitissymptom', 'ambition_subject.significantdiagnoses']
        self.sync_test_helper.sync_test_natural_key_attr(
            'ambition_subject')

    @tag('natural_key')
    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr('ambition_subject')
