from edc_visit_schedule.visit import Crf

# crfs = (
#     Crf(show_order=10, model='ambition_subject.someform',
#         required=False, additional=True),
# )

crfs_d5 = ()

crfs_d1 = (
    Crf(show_order=6, model='ambition_subject.patienthistory'),
    Crf(show_order=7, model='ambition_subject.lambarpuncturecsf'),
    Crf(show_order=8, model='ambition_subject.radiology'))

crfs_d3 = (Crf(show_order=1, model='ambition_subject.lambarpuncturecsf'),)

crfs_d5 = ()

crfs_d7 = (Crf(show_order=2, model='ambition_subject.lambarpuncturecsf'),)

crfs_d10 = ()

crfs_d12 = ()

crfs_d14 = (
    Crf(show_order=3, model='ambition_subject.lambarpuncturecsf'),)

crfs_w4 = (
    Crf(show_order=4, model='ambition_subject.week4'),)

crfs_w6 = ()

crfs_w8 = ()

crfs_w10 = ()
