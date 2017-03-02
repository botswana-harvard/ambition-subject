from edc_visit_schedule.visit import Requisition

from ..labs import viral_load_panel

requisitions = (
    Requisition(
        show_order=20, model='ambition_subject.subjectrequisition',
        panel=viral_load_panel, required=False, additional=False),
)
