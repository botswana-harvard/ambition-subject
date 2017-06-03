from django.test import TestCase, tag
from django.utils import timezone

from model_mommy import mommy
from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES
from edc_visit_tracking.constants import SCHEDULED

from ..models import FollowUp, Appointment
from ..forms import FollowUpForm


@tag('t')
class TestFollowUpForm(TestCase):

    def setUp(self):
        screening = mommy.make_recipe('ambition_screening.subjectscreening',
                                      report_datetime=get_utcnow())
        consent = mommy.make_recipe('ambition_subject.subjectconsent',
                                    consent_datetime=get_utcnow(),
                                    subject_screening=screening)
        visit_code = '1042'

        for app in Appointment.objects.all():
            self.subject_visit = mommy.make_recipe(
                'ambition_subject.subjectvisit',
                appointment=app,
                subject_identifier=consent.subject_identifier,
                reason=SCHEDULED,)
            if app.visit_code == visit_code:
                break

    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = FollowUpForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_no_diagnosis_date_with_no_significant_new_diagnosis(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'other_significant_new_diagnosis': NO,
                     'diagnosis_date': None})
        form = FollowUpForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_diagnosis_date_with_nos_significant_new_diagnosis(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'other_significant_new_diagnosis': YES,
                     'diagnosis_date': timezone.now().date()})
        form = FollowUpForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_no_fluconazole_dose_no_reason_given(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'fluconazole_dose': None,
                     'other_fluconazole_dose_reason': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())

    @tag('t')
    def test_is_rifampicin_started_with_day_started(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'rifampicin_started': NO,
                     'rifampicin_start_date': None})
        form = FollowUpForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_is_rifampicin_started_no_day_started(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'rifampicin_started': YES,
                     'rifampicin_start_date': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())

    def test_tb_pulmonary_dx(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'tb_pulmonary_dx': YES,
                     'tb_pulmonary_dx_date': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())

    def test_extra_pulmonary_tb_dx(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'extra_pulmonary_tb_dx': YES,
                     'extra_tb_pulmonary_dx_date': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())

    def test_kaposi_sarcoma_dx(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'kaposi_sarcoma_dx': YES,
                     'kaposi_sarcoma_dx_date': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())

    def test_bacteraemia_dx(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'bacteraemia_dx': YES,
                     'bacteraemia_dx_date': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())

    def test_pneumonia_dx(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'pneumonia_dx': YES,
                     'pneumonia_dx_date': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())

    def test_diarrhoeal_wasting_dx(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'diarrhoeal_wasting_dx': YES,
                     'diarrhoeal_wasting_dx_date': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())
