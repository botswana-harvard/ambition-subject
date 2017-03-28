from edc_visit_schedule.visit import Requisition

from ..labs import viral_load_panel

requisitions = (
    Requisition(
        show_order=20, model='ambition_subject.subjectrequisition',
        panel=viral_load_panel, required=False, additional=False),
)

# TODO: Add day 5 Chemistry requisition, Only form required
# TODO: Add day 7 FBC, ALT, CSF,and Chemistry requisitions
# TODO: Add day 10 Chemistry requisition, Only form required
# TODO: Add day 12 Chemistry requisition, Only form required
# TODO: Add day 14FBC, ALT, CSF,and Chemistry requisitions
# TODO: Add week 4 FBC, ALT and Chemistry requisitions
