
from django.utils.translation import ugettext as _

from edc_constants.constants import OTHER

VISIT_UNSCHEDULED_REASON = (
    ('Routine oncology',
     _('Routine oncology clinic visit (i.e. planned chemo, follow-up)')),
    ('Ill oncology', _('Ill oncology clinic visit')),
    ('Patient called', _('Patient called to come for visit')),
    (OTHER, _('Other, specify:')),
)

AE_SEVERITY = (
    ('Grade 3'), _('Grade 3- Severe'),
    ('Grade 4'), _('Grade 4- Life-threatening'),
    ('Grade 5'), _('Grade 5- Death'))

AE_INTENSITY = (
    ('Mild'), _('Mild'),
    ('Moderate'), _('Moderate'),
    ('Severe'), _('Severe'))

PATIENT_TREATMENT_GROUP = (
    ('Regiment 1'), _('Regiment 1 (Ambisome 10 mg/kg day 1 (single dose))'),
    ('Regiment 2'), _('Regiment 2 (Ambisome 10 mg/kg day 1, Ambisome 5 mg/kg '
                      'day 3 (two doses))'),
    ('Regiment 3'), _('Regiment 3 (Ambisome 10 mg/kg day 1, Ambisome 5 mg/kg '
                      'days 3, and 7 (three doses))')
    ('Regiment 4'), _('Regimen 4 (Ambisome 3 mg/kg/d for 14 days '
                      '(standard dose, "control arm")))'))

STUDY_DRUG_RELATIONSHIP = (
    ('Not related'), _('Not related'),
    ('Unlikely related'), _('Unlikely related'),
    ('Possibly related'), _('Possibly related'),
    ('Probably related'), _('Probably related'),
    ('Definitely related'), _('Definitely related'),
    ('Not applicable'), _('NA'))

RAE_REASON = (
    ('Death'), _('Death (Please complete Death form and Study termination'
                 'form)'),
    ('Life-threatening'), _('Life-threatening'),
    ('Significant disability'), _('Significant disability'),
    ('In-patient hospitalization or prolongation'),
    _('In-patient hospitalization or prolongation '
      '(beyond 2 weeks from study inclusion)'),
    ('Medically important event'),
    _('Medically important event (e.g. Severe thrombophlebitis, Bacteraemia, '
      'recurrence of symptoms not requiring admission, Hospital acquired '
      'pneumonia)'))

ARV_REGIMEN = (
    ('TDF +3TC/FTC + either EFZ or NVP', _('TDF +3TC/FTC + either EFZ or NVP')),
    ('AZT + 3-TC + either EFV or NVP', _('AZT + 3-TC + either EFV or NVP')),
    ('d4T + 3-TC + either EFV or NVP', _('d4T + 3-TC + either EFV or NVP')),
    ('TDF + 3TC/FTC + either ATZ/r or Lopinavir/r',
     _('TDF + 3TC/FTC + either ATZ/r or Lopinavir/r')),
    ('AZT + 3TC + either ATZ/r or Lopinavir/r',
     _('AZT + 3TC + either ATZ/r or Lopinavir/r'))
)
FIRST_LINE_REGIMEN = (
    ('EFV', _('EFV')),
    ('NVP', _('NVP'))
)
TB_SITE = (
    ('Pulmonary', _('Pulmonary')),
    ('Extra pulmonary', _('Extra pulmonary')),
)
MEDICATION_HISTORY = (
    ('TMP-SMX', _('TMP-SMX')),
    (OTHER, _('Other, specify:')),
)
