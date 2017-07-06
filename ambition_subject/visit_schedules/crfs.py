from edc_visit_schedule.visit import Crf

crfs_d1 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.patienthistory'),
    Crf(show_order=3, model='ambition_subject.bloodresult'),
    Crf(show_order=4, model='ambition_subject.prnmodel'),
    Crf(show_order=5, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=6, model='ambition_subject.microbiology', required=False),
    Crf(show_order=7, model='ambition_subject.radiology', required=False),
    Crf(show_order=8, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=9, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=10, model='ambition_subject.deathreport', required=False))

crfs_d3 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.bloodresult'),
    Crf(show_order=3, model='ambition_subject.prnmodel'),
    Crf(show_order=4, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=5, model='ambition_subject.microbiology', required=False),
    Crf(show_order=6, model='ambition_subject.radiology', required=False),
    Crf(show_order=7, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=8, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=9, model='ambition_subject.deathreport', required=False))

crfs_d5 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.bloodresult'),
    Crf(show_order=3, model='ambition_subject.prnmodel'),
    Crf(show_order=4, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=5, model='ambition_subject.microbiology', required=False),
    Crf(show_order=6, model='ambition_subject.radiology', required=False),
    Crf(show_order=7, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=8, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=9, model='ambition_subject.deathreport', required=False))

crfs_d7 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.bloodresult'),
    Crf(show_order=3, model='ambition_subject.prnmodel'),
    Crf(show_order=4, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=5, model='ambition_subject.microbiology', required=False),
    Crf(show_order=6, model='ambition_subject.radiology', required=False),
    Crf(show_order=7, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=8, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=9, model='ambition_subject.deathreport', required=False))

crfs_d10 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.bloodresult'),
    Crf(show_order=3, model='ambition_subject.prnmodel'),
    Crf(show_order=4, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=5, model='ambition_subject.microbiology', required=False),
    Crf(show_order=6, model='ambition_subject.radiology', required=False),
    Crf(show_order=7, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=8, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=9, model='ambition_subject.deathreport', required=False))

crfs_d12 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.bloodresult'),
    Crf(show_order=3, model='ambition_subject.prnmodel'),
    Crf(show_order=4, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=5, model='ambition_subject.microbiology', required=False),
    Crf(show_order=6, model='ambition_subject.radiology', required=False),
    Crf(show_order=7, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=8, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=9, model='ambition_subject.deathreport', required=False))

crfs_d14 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.bloodresult'),
    Crf(show_order=3, model='ambition_subject.week2'),
    Crf(show_order=4, model='ambition_subject.prnmodel'),
    Crf(show_order=5, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=6, model='ambition_subject.microbiology', required=False),
    Crf(show_order=7, model='ambition_subject.radiology', required=False),
    Crf(show_order=8, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=9, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=10, model='ambition_subject.deathreport', required=False))

crfs_w4 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.week4'),
    Crf(show_order=3, model='ambition_subject.bloodresult'),
    Crf(show_order=4, model='ambition_subject.recurrencesymptom',
        required=False),
    Crf(show_order=5, model='ambition_subject.prnmodel'),
    Crf(show_order=6, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=7, model='ambition_subject.microbiology', required=False),
    Crf(show_order=8, model='ambition_subject.radiology', required=False),
    Crf(show_order=9, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=10, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=11, model='ambition_subject.deathreport', required=False))

crfs_w6 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.followup'),
    Crf(show_order=3, model='ambition_subject.recurrencesymptom',
        required=False),
    Crf(show_order=4, model='ambition_subject.prnmodel'),
    Crf(show_order=5, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=6, model='ambition_subject.microbiology', required=False),
    Crf(show_order=7, model='ambition_subject.radiology', required=False),
    Crf(show_order=8, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=9, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=10, model='ambition_subject.deathreport', required=False))

crfs_w8 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.followup'),
    Crf(show_order=3, model='ambition_subject.recurrencesymptom',
        required=False),
    Crf(show_order=4, model='ambition_subject.prnmodel'),
    Crf(show_order=5, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=6, model='ambition_subject.microbiology', required=False),
    Crf(show_order=7, model='ambition_subject.radiology', required=False),
    Crf(show_order=8, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=9, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=10, model='ambition_subject.deathreport', required=False))

crfs_w10 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.followup'),
    Crf(show_order=3, model='ambition_subject.studyterminationconclusion'),
    Crf(show_order=4, model='ambition_subject.recurrencesymptom',
        required=False),
    Crf(show_order=5, model='ambition_subject.prnmodel'),
    Crf(show_order=6, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=7, model='ambition_subject.microbiology', required=False),
    Crf(show_order=8, model='ambition_subject.radiology', required=False),
    Crf(show_order=9, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=10, model='ambition_subject.lumbarpuncturecsf',
        required=False),
    Crf(show_order=11, model='ambition_subject.deathreport',
        required=False))

crfs_w16 = (
    Crf(show_order=1, model='ambition_subject.clinicnote'),
    Crf(show_order=2, model='ambition_subject.week16'),
    Crf(show_order=3, model='ambition_subject.recurrencesymptom'),
    Crf(show_order=4, model='ambition_subject.prnmodel'),
    Crf(show_order=5, model='ambition_subject.adverseevent', required=False),
    Crf(show_order=6, model='ambition_subject.microbiology', required=False),
    Crf(show_order=7, model='ambition_subject.radiology', required=False),
    Crf(show_order=8, model='ambition_subject.protocoldeviationviolation',
        required=False),
    Crf(show_order=9, model='ambition_subject.lumbarpuncturecsf', required=False))
