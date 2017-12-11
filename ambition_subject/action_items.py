from ambition_ae.action_items import AeInitialAction
from ambition_screening import EarlyWithdrawalEvaluator
from ambition_visit_schedule import DAY1
from edc_action_item import Action, site_action_items, HIGH_PRIORITY
from edc_constants.constants import YES

from .constants import RECURRENCE_OF_SYMPTOMS_ACTION, STUDY_TERMINATION_CONCLUSION_ACTION


class RecurrenceOfSymptomsAction(Action):
    name = RECURRENCE_OF_SYMPTOMS_ACTION
    display_name = 'Submit Recurrence of Symptoms Report'
    model = 'ambition_subject.recurrencesymptom'
    show_on_dashboard = True
    priority = HIGH_PRIORITY


class StudyTerminationConclusionAction(Action):
    name = STUDY_TERMINATION_CONCLUSION_ACTION
    display_name = 'Submit Study Termination/Conclusion Report'
    model = 'ambition_subject.studyterminationconclusion'
    prn_form_action = True
    show_on_dashboard = True
    priority = HIGH_PRIORITY


class BloodResultAction(Action):
    name = 'abnormal-blood-result'
    display_name = 'Reportable Blood Result'
    model = 'ambition_subject.bloodresult'
    priority = HIGH_PRIORITY
    show_on_dashboard = True

    def get_next_actions(self):
        # early withdrawal if abnormal on DAY1
        if self.model_obj.subject_visit.visit_code == DAY1:
            evaluator = EarlyWithdrawalEvaluator(
                subject_identifier=self.model_obj.subject_identifier)
            if not evaluator.eligible:
                return [StudyTerminationConclusionAction]
        else:
            # AE for reportable result, not on DAY1
            if (self.model_obj.results_abnormal == YES
                    and self.model_obj.results_reportable == YES):
                return [AeInitialAction]
        return []


site_action_items.register(BloodResultAction)
site_action_items.register(StudyTerminationConclusionAction)
site_action_items.register(RecurrenceOfSymptomsAction)
