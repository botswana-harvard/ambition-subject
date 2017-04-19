from model_mommy import mommy

from django.test import TestCase, tag

from edc_constants.constants import NO


@tag('screening')
class TestSubjectScreening(TestCase):

    def test_subject_ineligible_lt_18_years(self):
        """Test eligibility of a participant with under age."""
        options = {'age': 16, 'willing_to_give_informed_consent': NO}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subject_screening', **options)
        self.assertIn(subject_screening.ineligibility, 'Participant is under 18')
        self.assertFalse(subject_screening.is_eligible)
