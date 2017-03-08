from edc_constants.constants import OTHER, NOT_APPLICABLE

VISIT_UNSCHEDULED_REASON = (
    ('routine_oncology',
     'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
    ('ill_oncology', 'Ill oncology clinic visit'),
    ('patient_called', 'Patient called to come for visit'),
    (OTHER, 'Other, specify:'))

AE_SEVERITY = (
    ('grade_3', 'Grade 3- Severe'),
    ('grade_4', 'Grade 4- Life-threatening'),
    ('grade_5', 'Grade 5- Death'))

AE_INTENSITY = (
    ('mild', 'Mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'))

PATIENT_TREATMENT_GROUP = (
    ('regimen_1', 'Regimen 1 (Ambisome 10 mg/kg day 1 (single dose))'),
    ('regimen_2', 'Regimen 2 (Ambisome 10 mg/kg day 1, Ambisome 5 mg/kg day 3 '
                  '(two doses))'),
    ('regimen_3', 'Regimen 3 (Ambisome 10 mg/kg day 1, Ambisome 5 mg/kg days '
                  '3, and 7 (three doses))'),
    ('regimen_4', 'Regimen 4 (Ambisome 3 mg/kg/d for 14 days (standard dose'
                  ', control arm))'))

STUDY_DRUG_RELATIONSHIP = (
    ('not_related', 'Not related'),
    ('unlikely_related', 'Unlikely related'),
    ('possibly_related', 'Possibly related'),
    ('probably_related', 'Probably related'),
    ('definitely_related', 'Definitely related'),
    (NOT_APPLICABLE, 'Not Applicable'))

RAE_REASON = (
    ('death', 'Death (Please complete Death form and Study termination form)'),
    ('life_threatening', 'Life-threatening'),
    ('significant_disability', 'Significant disability'),
    ('in-patient_hospitalization or prolongation',
     'In-patient hospitalization or prolongation '
     '(beyond 2 weeks from study inclusion)'),
    ('Medically_important_event',
     'Medically important event (e.g. Severe thrombophlebitis, Bacteraemia, '
     'recurrence of symptoms not requiring admission, Hospital acquired '
     'pneumonia)'))

ARV_REGIMEN = (
    ('TDF +3TC/FTC + either EFZ or NVP', 'TDF +3TC/FTC + either EFZ or NVP'),
    ('AZT + 3-TC + either EFV or NVP', 'AZT + 3-TC + either EFV or NVP'),
    ('d4T + 3-TC + either EFV or NVP', 'd4T + 3-TC + either EFV or NVP'),
    ('TDF + 3TC/FTC + either ATZ/r or Lopinavir/r',
     'TDF + 3TC/FTC + either ATZ/r or Lopinavir/r'),
    ('AZT + 3TC + either ATZ/r or Lopinavir/r',
     'AZT + 3TC + either ATZ/r or Lopinavir/r'))

FIRST_LINE_REGIMEN = (
    ('EFV', 'EFV'),
    ('NVP', 'NVP'))

TB_SITE = (
    ('pulmonary', 'Pulmonary'),
    ('extra_pulmonary', 'Extra pulmonary'))

MEDICATION_HISTORY = (
<<<<<<< HEAD
    ('TMP-SMX', _('TMP-SMX')),
    (OTHER, _('Other, specify:')),
)
PROTOCOL_VIOLATION = (
    ('failure_to_obtain_informed_consent', 
     _('Failure to obtain informed consent')),
    ('enrollment_of_ineligible_patient', _('Enrollment of ineligible patient')),
    ('screening_procedure not done',
     _('Screening procedure required by protocol not done')),
    ('screening_or_on-study_procedure',
     _('Screening or on-study procedure/lab work required not done')),
    ('incorrect_research_treatment',
     _('Incorrect research treatment given to patient')),
    ('procedure_not_completed',
     _('On-study procedure required by protocol not completed')),
    ('visit_non-compliance', _('Visit non-compliance')),
    ('medication_stopped_early', _('Medication stopped early')),
    ('medication_noncompliance', _('Medication_noncompliance')),
    ('national_regulations_not_met',
     _('Standard WPD, ICH-GCP, local/national regulations not met')),
    (OTHER, _('Other'))
)
ACTION_REQUIRED = (
    ('participant_to_remain', _('Participant to remain on trial')),
    ('participant_to_be_withdrawn', _('participant to be withdrawn from trial')),
    ('patient_remains_on_study',
     _('Patient remains on study but data analysis will be modified'))
)
=======
    ('TMP-SMX', 'TMP-SMX'),
    (OTHER, 'Other, specify:'))
>>>>>>> a3bf382ad1b73d2f7d3803023ab0a46d5ce2f7d5
