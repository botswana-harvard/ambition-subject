from edc_visit_schedule.visit import Crf

# crfs = (
#     Crf(show_order=10, model='ambition_subject.someform',
#         required=False, additional=True),
# )

crfs = ()

day1_crfs = (
    Crf(show_order=10, model='ambition_subject.patienthistory'),
    Crf(show_order=20, model='ambition_subject.lambarpuncturecsf'),
    Crf(show_order=30, model='ambition_subject.radiology'))

day3_crfs = (Crf(show_order=10, model='ambition_subject.lambarpuncturecsf'))

day7_crfs = (Crf(show_order=10, model='ambition_subject.lambarpuncturecsf'))

day14_crfs = (
    Crf(show_order=10, model='ambition_subject.lambarpuncturecsf'),
    Crf(show_order=10, model='ambition_subject.week2'))

week4_crfs = (
    Crf(show_order=10, model='ambition_subject.week4'))

follow_up = (Crf(show_order=10, model='ambition_subject.followup'),)
