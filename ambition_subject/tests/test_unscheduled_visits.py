from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from model_mommy import mommy

from ambition_rando.import_randomization_list import import_randomization_list
from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.utils import get_utcnow
from edc_visit_tracking.constants import UNSCHEDULED, SCHEDULED

from ..models import Appointment
from ..models.model_mixins import UnscheduledAppointment, WrongAppointmentError


@tag('ap')
class TestUnscheduledVisits(TestCase, CreateAppointmentsMixin):

    def setUp(self):
        import_randomization_list()
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening')
        self.consent = mommy.make_recipe('ambition_subject.subjectconsent',
                                         consent_datetime=(
                                             get_utcnow() - relativedelta(days=6)),
                                         subject_screening=subject_screening)

    def add_visits_inorder(self, visit_code):
        for app in Appointment.objects.all():
            self.subject_visit = mommy.make_recipe(
                'ambition_subject.subjectvisit',
                appointment=app,
                subject_identifier=self.consent.subject_identifier,
                reason=SCHEDULED,)
            if app.visit_code == visit_code:
                return app

    def test_unscheduled_appointment_before_1014(self):
        apppointment = self.add_visits_inorder('1012')
        self.assertRaises(
            WrongAppointmentError, UnscheduledAppointment(apppointment))

    def test_create_new_appointment(self):
        appointment = self.add_visits_inorder('1028')

        UnscheduledAppointment(appointment)
        self.assertEqual(Appointment.objects.filter(
            subject_identifier=self.consent.subject_identifier,
            visit_code__contains='1028').count(), 2)
        self.tearDown()
