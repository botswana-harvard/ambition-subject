import sys

from django.core.management.color import color_style

from edc_visit_schedule.visit_schedule import VisitSchedule
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .schedule import schedule

style = color_style()

visit_schedule = VisitSchedule(
    name='visit_schedule',
    verbose_name='Ambition',
    app_label='ambition_subject',
    default_enrollment_model='ambition_subject.enrollment',
    default_disenrollment_model='ambition_subject.disenrollment',
    visit_model='ambition_subject.subjectvisit',
    offstudy_model='ambition_subject.subjectoffstudy',
)
visit_schedule.add_schedule(schedule)

site_visit_schedules.register(visit_schedule)
