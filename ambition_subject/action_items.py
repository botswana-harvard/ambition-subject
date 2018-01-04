from ambition_ae.action_items import AeInitialAction
from ambition_prn.action_items import StudyTerminationConclusionAction
from ambition_screening import EarlyWithdrawalEvaluator
from ambition_visit_schedule import DAY1
from edc_action_item import Action, site_action_items, HIGH_PRIORITY
from edc_constants.constants import YES

BLOOD_RESULTS_ACTION = 'abnormal-blood-result'
RECONSENT_ACTION = 'reconsent'


class BloodResultAction(Action):
    name = BLOOD_RESULTS_ACTION
    display_name = 'Reportable Blood Result'
    model = 'ambition_subject.bloodresult'
    priority = HIGH_PRIORITY
    show_on_dashboard = True
    create_by_user = False

    def get_next_actions(self):
        # early withdrawal if qualifying blood results
        # are abnormal on DAY1
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


class ReconsentAction(Action):
    name = RECONSENT_ACTION
    display_name = 'Re-consent participant'
    model = 'ambition_subject.subjectreconsent'
    priority = HIGH_PRIORITY
    show_on_dashboard = True
    show_link_to_changelist = True
    admin_site_name = 'ambition_subject_admin'
    create_by_user = False
    singleton = True
    instructions = (
        'Participant must be re-consented as soon as able. '
        'Participant\'s ICF was initially completed by next-of-kin.')


site_action_items.register(BloodResultAction)
site_action_items.register(ReconsentAction)
