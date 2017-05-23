from django.test import TestCase, tag
from django.utils import timezone

from model_mommy import mommy
from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES

from ..models import FollowUp
from ..forms import FollowUpForm
from ambition_subject.models.appointment import Appointment
from edc_visit_tracking.constants import SCHEDULED


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

        self.significantnewdiagnosis = mommy.make_recipe('ambition_subject.significantnewdiagnosis')

    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                    'significant_new_diagnosis': [self.significantnewdiagnosis.id]})
        form = FollowUpForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_no_diagnosis_date_with_other_significant_new_diagnosis(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                    'significant_new_diagnosis': [self.significantnewdiagnosis.id],
                     'other_significant_new_diagnosis': YES,
                     'diagnosis_date': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())

    def test_no_diagnosis_date_with_no_significant_new_diagnosis(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                    'significant_new_diagnosis': [self.significantnewdiagnosis.id],
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
                    'significant_new_diagnosis': [self.significantnewdiagnosis.id],
                     'other_significant_new_diagnosis': YES,
                     'diagnosis_date': timezone.now().date()})
        form = FollowUpForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_fluconazole_dose_no_reason_given(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                    'significant_new_diagnosis': [self.significantnewdiagnosis.id],
                     'fluconazole_dose': '400mg_daily',
                     'other_fluconazole_dose_reason': None})
        form = FollowUpForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_no_fluconazole_dose_no_reason_given(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                    'significant_new_diagnosis': [self.significantnewdiagnosis.id],
                     'fluconazole_dose': None,
                     'other_fluconazole_dose_reason': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())

    def test_is_rifampicin_started_with_day_started(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                    'significant_new_diagnosis': [self.significantnewdiagnosis.id],
                     'is_rifampicin_started': NO,
                     'study_day_rifampicin_started': None})
        form = FollowUpForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_is_rifampicin_started_no_day_started(self):
        obj = mommy.prepare_recipe(FollowUp._meta.label_lower,)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id,
                    'significant_new_diagnosis': [self.significantnewdiagnosis.id],
                     'is_rifampicin_started': YES,
                     'study_day_rifampicin_started': None})
        form = FollowUpForm(data=data)
        self.assertFalse(form.is_valid())


