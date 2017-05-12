from datetime import datetime

from django.test import TestCase, tag
from model_mommy import mommy

from edc_constants.constants import YES, NO

from ..forms import DeathForm


@tag('death')
class TestDeath(TestCase):

    def setUp(self):
        super().setUp()
#
#         self.household_member = HouseholdMember.objects.filter(
#             subject_identifier=self.subject_visit)

#         self.death = mommy.make_recipe('ambition_subject.death')

        self.data = {
            'date_of_death': datetime.utcnow(),
            'study_day': '03',
            'death_as_inpatient': YES,
            'cause_of_death_study_doctor_opinion': 'cryptococcal_meningitis',
            'cause_other_study_doctor_opinion': None,
            'cause_tb_study_doctor_opinion': 'pulmonary',
            'cause_of_death_tmg1_opinion': 'cryptococcal_meningitis',
            'cause_of_death_agreed': YES,
            'cause_other_tmg1_opinion': None,
            'cause_tb_tmg1_opinion': 'meningitis',
            'cause_of_death_tmg2_opinion': 'cryptococcal_meningitis',
            'cause_other_tmg2_opinion': None,
            'cause_tb_tmg2_opinion': 'pulmonary',
            'narrative_summary': 'adverse event resulted in death due to cryptococcal meningitis',
            'report_datetime': datetime.utcnow(),
        }

    def test_valid_form(self):
        form = DeathForm(data=self.data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_cause_of_death_agreed(self):
        """
        Assert that cause of death agreed between Study dr and TMG member
        """
        self.data.update(cause_of_death_agreed=YES)
        form = DeathForm(data=self.data)
        self.assertTrue(form.is_valid())
 
    def test_cause_of_death_not_agreed(self):
        """
        Assert that cause of death agreed between Study dr and TMG member
        """
        self.data.update(cause_of_death_agreed=YES, cause_of_death_tmg2_opinion=None)
        form = DeathForm(data=self.data)
        self.assertFalse(form.is_valid())
 
    def test_cause_of_death_study_dr_opinion_other_required(self):
        """
        Assert that cause of death study dr and tmg member opinion not needed
        """
        self.data.update(cause_of_death_agreed=NO, cause_other_study_doctor_opinion=None)
        form = DeathForm(data=self.data)
        self.assertFalse(form.is_valid())
