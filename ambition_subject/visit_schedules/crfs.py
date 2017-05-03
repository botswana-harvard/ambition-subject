from edc_visit_schedule.visit import Crf

# crfs = (
#     Crf(show_order=10, model='ambition_subject.someform',
#         required=False, additional=True),
# )

crfs_d1 = (
    Crf(show_order=1, model='ambition_subject.subjectrandomization'),
    Crf(show_order=2, model='ambition_subject.bloodresult'),
    Crf(show_order=3, model='ambition_subject.patienthistory'),
    Crf(show_order=4, model='ambition_subject.lumbarpuncturecsf'),
    Crf(show_order=5, model='ambition_subject.radiology'))

crfs_d3 = (Crf(show_order=1, model='ambition_subject.clinicnote'),)

crfs_d5 = (Crf(show_order=1, model='ambition_subject.clinicnote'),)

crfs_d7 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.lumbarpuncturecsf'),)

crfs_d10 = (Crf(show_order=1, model='ambition_subject.clinicnote'),)

crfs_d12 = (Crf(show_order=1, model='ambition_subject.clinicnote'),)

crfs_d14 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.week2'),
    Crf(show_order=3, model='ambition_subject.lumbarpuncturecsf'),)

crfs_w4 = (
    Crf(show_order=1, model='ambition_subject.week4'),)

crfs_w6 = (Crf(show_order=1, model='ambition_subject.followup'),)

crfs_w8 = (Crf(show_order=1, model='ambition_subject.followup'),)

crfs_w10 = (Crf(show_order=1, model='ambition_subject.followup'),)
