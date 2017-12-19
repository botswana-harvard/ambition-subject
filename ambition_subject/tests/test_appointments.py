from ambition_rando.import_randomization_list import import_randomization_list
from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_facility.holidays import Holidays
from model_mommy import mommy


class TestAppointment(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening')
        options = {
            'screening_identifier': subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        consent = mommy.make_recipe(
            'ambition_subject.subjectconsent', **options)
        self.subject_identifier = consent.subject_identifier

    def test_appointments_creation(self):
        """Assert appointment triggering method creates appointments.
        """
        appointments = Appointment.objects.filter(
            subject_identifier=self.subject_identifier)
        self.assertEqual(appointments.count(), 12)

    def test_appointments_rdates(self):
        holidays = Holidays(country='botswana')
        appointments = Appointment.objects.filter(
            subject_identifier=self.subject_identifier).order_by('appt_datetime')
        appt_datetimes = [obj.appt_datetime for obj in appointments]
        start = appt_datetimes[0]
        if not holidays.is_holiday(start + relativedelta(days=2)):
            self.assertEqual(appt_datetimes[1].date(
            ), start.date() + relativedelta(days=2))
        if not holidays.is_holiday(start + relativedelta(days=4)):
            self.assertEqual(appt_datetimes[2].date(
            ), start.date() + relativedelta(days=4))
        if not holidays.is_holiday(start + relativedelta(days=6)):
            self.assertEqual(appt_datetimes[3].date(
            ), start.date() + relativedelta(days=6))
