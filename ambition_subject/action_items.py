from edc_action_item.action import Action
from edc_action_item.constants import HIGH_PRIORITY
from ambition_ae.action_items import AeInitialAction
from edc_constants.constants import YES


class BloodResultAction(Action):
    name = 'abnormal-blood-result'
    display_name = 'Reportable Blood Result'
    model = 'ambition_subject.bloodresult'
    show_on_dashboard = False
    priority = HIGH_PRIORITY
    prn_form_action = True
    show_on_dashboard = True

    def get_next_actions(self):
        if (self.model_obj.results_abnormal == YES
                and self.model_obj.results_reportable == YES):
            return [AeInitialAction]
        return []
