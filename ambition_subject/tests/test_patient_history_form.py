from django.test import TestCase

from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_constants.constants import NO, NOT_APPLICABLE, OTHER, YES
from edc_visit_tracking.constants import SCHEDULED

from ..models import Appointment
from ambition_subject.models.patient_history import PatientHistory
from ambition_subject.forms.patient_history_form import PatientHistoryForm
from ambition_subject.mommy_recipes import DateProvider


class TestPatientHistory(TestCase):

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

        self.neurological = mommy.make_recipe('ambition_subject.neurological')

    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_has_tb_history_tb_site_specified(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_has_tb_history_no_tb_site_specified(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'med_history': YES,
                     'tb_site': None})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

    def test_taking_rifampicin_while_on_tb_treatment(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'tb_treatment': YES,
                     'taking_rifampicin': None})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'tb_treatment': YES,
                     'taking_rifampicin': NO})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'tb_treatment': NO,
                     'taking_rifampicin': NOT_APPLICABLE})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_give_date_started_while_taking_rifampicin(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'taking_rifampicin': YES,
                     'rifampicin_started_date': None})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'taking_rifampicin': YES,
                     'rifampicin_started_date': DateProvider.next_month(self)})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'taking_rifampicin': YES,
                     'rifampicin_started_date': DateProvider.yesterday(self)})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'taking_rifampicin': NO,
                     'rifampicin_started_date': None})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_give_date_for_previous_infection(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'previous_infection': YES,
                     'infection_date': None})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'previous_infection': YES,
                     'infection_date': DateProvider.next_month(self)})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'previous_infection': YES,
                     'infection_date': DateProvider.yesterday(self),
                     'previous_infection_specify': 'ashma'})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'previous_infection': NO,
                     'infection_date': None})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_new_hiv_diagnosis_arv_treatment(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'taking_arv': YES,
                     'arv_date': None})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'taking_arv': YES,
                     'arv_date': DateProvider.next_month(self)})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'taking_arv': YES,
                     'arv_date': DateProvider.last_year(self)})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'taking_arv': NO,
                     'arv_date': None})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_first_line_arvs_and_other_specified(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'first_line_arvs': OTHER,
                    'first_line_arvs_other': None})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'first_line_arvs': OTHER,
                     'first_line_arvs_other': 'anti retro virals'})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_second_line_arvs_and_other_specified(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'second_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                    'second_line_arvs_other': None})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'second_line_arvs': OTHER,
                     'second_line_arvs_other': 'anti retro virals'})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

    def test_first_line_in_efv_npv_dtg(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                    'first_line_choice': None})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                     'first_line_choice': 'EFV'})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'first_line_arvs': 'AZT + 3-TC + either EFV or NVP or DTG',
                     'first_line_choice': NOT_APPLICABLE})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

    def test_patient_adherence_is_last_dose_given(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'patient_adherence': YES,
                    'last_dose': 3})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'patient_adherence': YES,
                    'last_dose': None})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'patient_adherence': NO,
                    'last_dose': 3})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'patient_adherence': NO,
                    'last_dose': None})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())

    def test_if_other_medications_list_other_medications(self):
        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'other_medications': NO,
                     'specify_medications': None})
        form = PatientHistoryForm(data=data)
        self.assertTrue(form.is_valid())

        obj = mommy.prepare_recipe(PatientHistory._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                     'other_medications': NO,
                     'specify_medications': 'TMP-SMX'})
        form = PatientHistoryForm(data=data)
        self.assertFalse(form.is_valid())
