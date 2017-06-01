from django.test import TestCase

from model_mommy import mommy

from edc_constants.constants import YES
from edc_base.utils import get_utcnow
from edc_visit_tracking.constants import SCHEDULED

from ..forms import LumbarPunctureCSFForm
from ..models import Appointment, LumbarPunctureCsf


class TestLumbarPunctureForm(TestCase):

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
        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_csf_culture_other(self):
        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_culture=YES,
                                   other_csf_culture=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_culture=YES,
                                   other_csf_culture='blahblah')
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertTrue(form.is_valid())

    def test_csf_wbc_cell_count(self):
        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=2)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=0,
                                   differential_lymphocyte_count=None,
                                   differential_neutrophil_count=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertTrue(form.is_valid())

    def test_differential_lymphocyte_count(self):
        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=6,
                                   differential_lymphocyte_count=None,
                                   differential_neutrophil_count=4)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=6,
                                   differential_lymphocyte_count=4,
                                   differential_neutrophil_count=4)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertTrue(form.is_valid())

    def test_differential_neutrophil_count(self):
        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=6,
                                   differential_lymphocyte_count=4,
                                   differential_neutrophil_count=None)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(LumbarPunctureCsf._meta.label_lower,
                                   csf_wbc_cell_count=6,
                                   differential_lymphocyte_count=4,
                                   differential_neutrophil_count=4)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = LumbarPunctureCSFForm(data=data)
        self.assertTrue(form.is_valid())
