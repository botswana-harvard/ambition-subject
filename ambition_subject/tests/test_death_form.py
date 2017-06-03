from model_mommy import mommy

from django.test import TestCase

from ..models import Death
from ..forms import DeathForm


class TestDeath(TestCase):

    def test_valid_form(self):
        obj = mommy.prepare_recipe(Death._meta.label_lower)
        form = DeathForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_tb_as_death_cause_tb_site_specified(self):
        """ Assert that if cause of death is TB, site of TB disease is specified.
        """
        obj = mommy.prepare_recipe(Death._meta.label_lower,
                                   cause_of_death_study_doctor_opinion='TB',
                                   cause_of_death_tmg1_opinion='TB',
                                   cause_of_death_tmg2_opinion='TB',
                                   cause_tb_study_doctor_opinion=None,
                                   cause_tb_tmg1_opinion=None,
                                   cause_tb_tmg2_opinion=None)
        form = DeathForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_tb_as_death_cause_th_site_not_specified(self):
        """ Assert that if cause of death is TB, site of TB disease is not
            specified.
        """
        obj = mommy.prepare_recipe(Death._meta.label_lower,
                                   cause_of_death_study_doctor_opinion='TB',
                                   cause_of_death_tmg1_opinion='TB',
                                   cause_of_death_tmg2_opinion='TB',
                                   cause_tb_study_doctor_opinion='pulmonary',
                                   cause_tb_tmg1_opinion='disseminated',
                                   cause_tb_tmg2_opinion='meningitis')
        form = DeathForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

