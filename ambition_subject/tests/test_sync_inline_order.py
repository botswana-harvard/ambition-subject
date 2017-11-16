from ambition_rando.import_randomization_list import import_randomization_list
from ambition_subject.forms import PreviousOpportunisticInfectionForm
from ambition_subject.models import PatientHistory, PreviousOpportunisticInfection
from django.forms import inlineformset_factory
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import NO, NOT_APPLICABLE
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy


class TestSyncInlineOrder(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        screening = mommy.make_recipe('ambition_subject.subjectscreening',
                                      report_datetime=get_utcnow())
        self.consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            screening_identifier=screening.screening_identifier)

        self.appointment = Appointment.objects.get(
            visit_code='1000', subject_identifier=self.consent.subject_identifier)
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=self.appointment,
            reason=SCHEDULED)

    def test_inline_order_outgoing(self):
        options = {'taking_arv': NOT_APPLICABLE,
                   'new_hiv_diagnosis': NO,
                   'subject_visit': self.subject_visit,
                   'report_datetime': get_utcnow()}
#         patient_history = mommy.prepare_recipe(
#             'ambition_subject.patienthistory', **options)
#         patient_history_form = PatientHistoryForm(
#             data=patient_history.__dict__)
        PatientHistoryFormSet = inlineformset_factory(
            PatientHistory,
            PreviousOpportunisticInfection,
            form=PreviousOpportunisticInfectionForm, extra=1)
        patient_history_form = PatientHistoryFormSet()
        print(patient_history_form)

#         obj_inline = PreviousOpportunisticInfection(
#             patient_history=patient_history
#         )
#         self.assertTrue(obj_inline)
