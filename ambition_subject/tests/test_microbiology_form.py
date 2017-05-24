from django.test import TestCase

from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_constants.constants import NO, NOT_APPLICABLE, OTHER, POS, YES
from edc_visit_tracking.constants import SCHEDULED

from ..constants import BACTERIA
from ..forms import MicrobiologyForm
from ..models import Appointment, Microbiology


class TestMicrobiology(TestCase):

    def setUp(self):
        screening = mommy.make_recipe(
            'ambition_screening.subjectscreening',
            report_datetime=get_utcnow())
        consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            subject_screening=screening)
        appointment = Appointment.objects.get(
            visit_code='1000')
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=appointment,
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED,)

    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_urine_culture_no_results_invalid(self):
        """ Assert results are provided for urine culture.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results=NOT_APPLICABLE)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results='no_growth')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_urine_culture_no_organism_invalid(self):
        """ Assert culture organism is specified for a
        urine culture result.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results=POS,
                                   urine_culture_organism=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results=POS,
                                   urine_culture_organism='e.coli')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_urine_culture_not_performed(self):
        """ Assert urine culture not perfomed is valid.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=NO,
                                   urine_culture_results=NOT_APPLICABLE,
                                   urine_culture_organism=NOT_APPLICABLE)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_urine_culture_no_organism_other(self):
        """ Assert urine culture organism other value is specified.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results=POS,
                                   urine_culture_organism=OTHER,
                                   urine_culture_organism_other=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   urine_culture_performed=YES,
                                   urine_culture_results=POS,
                                   urine_culture_organism=OTHER,
                                   urine_culture_organism_other='blahblah')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_blood_culture_no_results(self):
        """ Assert results are specified for a blood culture
        performed.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=NOT_APPLICABLE)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results='no_growth')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_blood_culture_no_study_day(self):
        """ Assert date blood was taken is specified.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=POS,
                                   blood_culture_organism='e.coli',
                                   date_blood_taken=NOT_APPLICABLE,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=POS,
                                   blood_culture_organism=(
                                       'cryptococcus_neoformans'),
                                   date_blood_taken=get_utcnow().date(),)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_blood_culture_no_organism(self):
        """ Assert organism is specified for a blood culture performed.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=POS,
                                   date_blood_taken=get_utcnow().date(),
                                   blood_culture_organism=NOT_APPLICABLE,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_results=POS,
                                   date_blood_taken=get_utcnow().date(),
                                   blood_culture_organism=(
                                       'cryptococcus_neoformans'),)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_blood_culture_no_organism_other(self):
        """ Assert other is specified if chosen for blood culture
        organism.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_organism=OTHER,
                                   blood_culture_organism_other=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_organism=OTHER,
                                   blood_culture_organism_other='blahblah')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_blood_culture_bacteria_specify(self):
        """ Assert other is specified if bacteria chosen
        for blood culture organism.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_organism=BACTERIA,
                                   bacteria_identified=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_organism=BACTERIA,
                                   blood_culture_organism_other='e.coli')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_blood_culture_bacteria_other(self):
        """ Assert other is specified if bacteria chosen for blood
        culture organism.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_organism=BACTERIA,
                                   bacteria_identified=OTHER,
                                   bacteria_identified_other=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   blood_culture_performed=YES,
                                   blood_culture_organism=BACTERIA,
                                   bacteria_identified=OTHER,
                                   bacteria_identified_other='blahblah')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_pos_sputum_no_results(self):
        """ Assert results are specified for positive sputum results.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   sputum_results_culture=POS,
                                   sputum_results_positive=None,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   sputum_results_culture=POS,
                                   sputum_results_positive='blahblah',)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_tissue_biopsy_no_results(self):
        """ Assert results are specified for a tissue biopsy.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results='no_growth',)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_biopsy_culture_no_study_day(self):
        """ Assert date is specified for a biopsy taken.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   tissue_biopsy_organism='cryptococcus_neoformans',
                                   date_biopsy_taken=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   tissue_biopsy_organism='cryptococcus_neoformans',
                                   date_biopsy_taken=get_utcnow().date())
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_tissue_biopsy_no_organism(self):
        """ Assert organism is specified for a biopsy taken.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   date_biopsy_taken=get_utcnow().date(),
                                   tissue_biopsy_organism=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   date_biopsy_taken=get_utcnow().date(),
                                   tissue_biopsy_organism='cryptococcus_neoformans')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_tissue_biopsy_no_organism_other(self):
        """ Assert other is specified if chosen for tissue biopsy
        organism.
        """
        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   tissue_biopsy_organism=OTHER,
                                   date_biopsy_taken=get_utcnow().date(),
                                   tissue_biopsy_organism_other=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(Microbiology._meta.label_lower,
                                   tissue_biopsy_taken=YES,
                                   tissue_biopsy_results=POS,
                                   date_biopsy_taken=get_utcnow().date(),
                                   tissue_biopsy_organism=OTHER,
                                   tissue_biopsy_organism_other='blahblah')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = MicrobiologyForm(data=data)
        self.assertTrue(form.is_valid())
