from edc_visit_schedule.visit_schedule import VisitSchedule
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .schedule import schedule1

visit_schedule1 = VisitSchedule(
    name='visit_schedule1',
    verbose_name='Ambition',
    app_label='ambition_subject',
    default_enrollment_model='ambition_subject.enrollment',
    default_disenrollment_model='ambition_subject.disenrollment',
    visit_model='ambition_subject.subjectvisit',
    offstudy_model='ambition_subject.subjectoffstudy',
)
visit_schedule1.add_schedule(schedule1)

site_visit_schedules.register(visit_schedule1)
