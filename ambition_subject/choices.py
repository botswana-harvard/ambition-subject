from ambition_validators.constants import WORKING
from edc_constants.constants import NEG, OTHER, POS, NOT_APPLICABLE
from edc_constants.constants import NORMAL, IND, YES, NO, UNKNOWN
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED

from .constants import DEVIATION, VIOLATION, TUBERCULOSIS, RESULTS_UNKNOWN
from .constants import CONSENT_WITHDRAWAL, ROUTINE_APPT

ABNORMAL_RESULTS_REASON = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('cerebral_oedema', 'Cerebral oedema'),
    ('hydrocephalus', 'Hydrocephalus'),
    ('cryptococcomus', 'Cryptococcomus'),
    ('dilated_virchow_robin_spaces', 'Dilated Virchow robin spaces'),
    ('enhancing_mass_lesions',
     'Enhancing mass lesions DD Toxoplasmosis, TB, lymphoma'),
    ('infarcts', 'Infarcts'),
    (OTHER, 'Other'))

ACTION_REQUIRED = (
    ('participant_to_remain', 'Participant to remain on trial'),
    ('participant_to_be_withdrawn', 'participant to be withdrawn from trial'),
    ('patient_remains_on_study',
     'Patient remains on study but data analysis will be modified')
)

ACTIVITIES_MISSED = (
    (WORKING, 'Working'),
    ('Studying', 'Studying'),
    ('Caring for Children', 'Caring for children'),
    ('Maintaining the house', 'Maintaining the house'),
    ('Nothing', 'Nothing'),
    (OTHER, 'Other'),
)


ANTIBIOTICS = (
    ('amoxicillin', 'Amoxicillin'),
    ('doxycycline', 'Doxycycline'),
    ('flucloxacillin', 'Flucloxacillin'),
    ('ceftriaxone', 'Ceftriaxone'),
    ('erythromycin',
     'Erythromycin (contra-indicated with concomitant high dose fluconazole)'),
    ('ciprofloxacin',
     'Ciprofloxacin (avoid with concomitant high dose fluconazole)'),
    (OTHER, 'Other'),
)

APPOINTMENT_REASON = (
    (ROUTINE_APPT, 'Routine'),
    (UNSCHEDULED, 'Unscheduled'),
)


ARV_REGIMEN = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('TDF +3TC/FTC + either EFV or NVP',
     'TDF +3TC/FTC + either EFV or NVP or DTG'),
    ('AZT + 3TC + either EFV or NVP or DTG',
     'AZT + 3TC + either EFV or NVP or DTG'),
    ('TDF + 3TC/FTC + either ATZ/r or Lopinavir/r',
     'TDF + 3TC/FTC + either ATZ/r or Lopinavir/r'),
    ('AZT + 3TC + either ATZ/r or Lopinavir/r',
     'AZT + 3TC + either ATZ/r or Lopinavir/r'),
    (OTHER, 'Other'),
)

FIRST_ARV_REGIMEN = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('TDF +3TC/FTC + either EFV or NVP',
     'TDF +3TC/FTC + either EFV or NVP or DTG'),
    ('AZT+3TC+ either EFV or NVP or DTG',
     'AZT+3TC+ either EFV or NVP or DTG'),
    (OTHER, 'Other'),
)

SECOND_ARV_REGIMEN = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('TDF+3TC/FTC+ either ATZ/r or Lopinavir/r',
     'TDF+3TC/FTC+ either ATZ/r or Lopinavir/r'),
    ('AZT+3TC+ either ATZ/r or Lopinavir/r',
     'AZT+3TC+ either ATZ/r or Lopinavir/r'),
    (OTHER, 'Other'),
)

BLOOD_CULTURE_RESULTS_ORGANISM = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('cryptococcus_neoformans', 'Cryptococcus neoformans'),
    ('bacteria', 'Bacteria'),
    ('bacteria_and_cryptococcus', 'Bacteria and Cryptococcus'),
    (OTHER, 'Other'),
)

BIOPSY_RESULTS_ORGANISM = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('cryptococcus_neoformans', 'Cryptococcus neoformans'),
    ('mycobacterium_tuberculosis', 'Mycobacterium Tuberculosis'),
    (OTHER, 'Other'),
)

BACTERIA_TYPE = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('e.coli', 'E.coli'),
    ('klebsiella_sp', 'Klebsiella sp'),
    ('streptococcus_pneumoniae', 'Streptococcus pneumoniae'),
    ('staphylococus_aureus', '(Sensitive) Staphylococus aureus'),
    ('mrsa', 'MRSA'),
    (OTHER, 'Other'),
)

BRAIN_IMAGINING_REASON = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('reduction_in_gcs', 'Reduction in GCS'),
    ('new_neurology', 'New neurology'),
    (OTHER, 'Other'),
)

CARE_PROVIDER = (
    ('doctor', 'Doctor'),
    ('clinical_officer', 'Clinical Officer'),
    ('nurse', 'Nurse'),
    ('traditional_healer', 'Traditional Healer'),
    ('spiritual_healer', 'Spiritual Healer'),
    ('family/friend', 'Family/Friend'),
    ('pharmacist', 'Pharmacist'),
    (OTHER, 'Other')
)

CAUSE_OF_DEATH = (
    ('cryptococcal_meningitis', 'Cryptococcal meningitis'),
    ('Cryptococcal_meningitis_relapse_IRIS',
     'Cryptococcal meningitis relapse/IRIS'),
    (TUBERCULOSIS, 'TB'),
    ('bacteraemia', 'Bacteraemia'),
    ('bacterial_pneumonia', 'Bacterial pneumonia'),
    ('malignancy', 'Malignancy'),
    ('art_toxicity', 'ART toxicity'),
    ('IRIS_non_CM', 'IRIS non-CM'),
    ('diarrhea_wasting', 'Diarrhea/wasting'),
    (UNKNOWN, 'Unknown'),
    (OTHER, 'Other'),
)

CN_PALSY = (
    ('III', 'III'),
    ('VI', 'VI'),
    ('VII', 'VII'),
    ('VIII', 'VIII'),
)

CLINICAL_ASSESSMENT = (
    (NOT_APPLICABLE, 'Not applicable'),
)

CULTURE_RESULTS = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('no_growth', 'No growth'),
    (POS, 'Positive'),
)

CURRENCY = (
    ('botswana_pula', 'Botswana Pula'),
    ('malawian_kwacha', 'Malawian Kwacha'),
    ('south_african_rand', 'South African Rand'),
    ('ugandan_shilling', 'Ugandan Shilling'),
    ('us_dollar', 'US Dollar'),
    ('zimbabwean_dollar', 'Zimbabwean Dollar'),
)

CXR_TYPE = (
    (NOT_APPLICABLE, 'Not Applicable'),
    (NORMAL, 'Normal'),
    ('hilar_adenopathy', 'Hilar adenopathy'),
    ('miliary_appearance', 'Miliary appearance'),
    ('pleural_effusion', 'Pleural effusion'),
    ('infiltrates', 'Infiltrates'),
)

DR_OPINION = (
    ('cm_release', 'CM Relapse'),
    ('cm_iris', 'CM IRIS'),
    (OTHER, 'Other'),
)

ECOG_SCORE = (
    ('0',
     'Fully active, able to carry on all pre-disease performance without restriction'),
    ('1', 'Restricted in physically strenuous activity but '
     'ambulatory and able to carry out work of a light or sedentary nature, e.g., '
     'light house work, office work'),
    ('2', 'Ambulatory and capable of all selfcare but unable to carry out '
     'any work activities;up and about more than 50% of waking hours '),
    ('3', 'Capable of only limited selfcare; confined to bed or chair more than '
     '50% of waking hours'),
    ('4',
     'Completely disabled; cannot carry on any selfcare; totally confined to bed or chair'),
    ('5', 'Dead'),
)

FIRST_LINE_REGIMEN = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('EFV', 'EFV'),
    ('DTG', 'DTG'),
    ('NVP', 'NVP'),
)

FLUCONAZOLE_DOSE = (
    ('800mg_daily', '800mg Daily'),
    (OTHER, 'Other'),
    ('Not Done', 'Not Done'),
)

FLUCYTOSINE_DOSE_MISSED = (
    ('dose_1', 'Dose 1'),
    ('dose_2', 'Dose 2'),
    ('dose_3', 'Dose 3'),
    ('dose_4', 'Dose 4')
)

GLASGOW_COMA_SCORE_EYES = (
    ('does_not_open_eyes', 'Does not open eyes'),
    ('opens_eyes_to_pain_only', 'Opens eyes to pain only'),
    ('opens_eyes_to_voice', 'Opens eyes to voice'),
    ('opens_eyes_spontaneously', 'Opens eyes spontaneously'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

GLASGOW_COMA_SCORE_VERBAL = (
    ('makes_no_sounds', 'Makes no sounds'),
    ('makes_sounds', 'Makes sounds'),
    ('makes_words', 'Makes words'),
    ('disoriented', 'Disoriented'),
    ('oriented', 'Oriented'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

GLASGOW_COMA_SCORE_MOTOR = (
    ('makes_no_movement', 'Makes no movement'),
    ('extension_to_pain', 'Extension to pain'),
    ('flexion_to_pain', 'Flexion to pain'),
    ('withdraws_from_pain', 'Withdraws from pain'),
    ('localizes_pain', 'Localizes pain'),
    ('obey_commands', 'Obey commands'),
)

ID_TYPE = (
    ('country_id', 'Country ID Number'),
    ('drivers', 'Driver\'s License'),
    ('passport', 'Passport'),
    ('hospital_no', 'Hospital Number'),
    ('country_id_rcpt', 'Country ID Receipt'),
    (OTHER, 'Other'),
)


INFECTION = (
    ('Kaposi_sarcoma', 'Kaposi Sarcoma'),
    ('Herpes_zoster_virus', 'Herpes Zoster Virus'),
    ('Oesophageal_candidiasis', 'Oesophageal Candidiasis'),
    ('PCP', 'PCP'),
    ('Cytomegalovirus', 'Cytomegalovirus'),
    (OTHER, 'Other')
)


INFILTRATE_LOCATION = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('lul', 'LUL'),
    ('lll', 'LLL'),
    ('rul', 'RUL'),
    ('rll', 'RLL'),
    ('rml', 'RML'),
    ('diffuse', 'Diffuse'),
)

INFO_SOURCE = (
    ('hospital_notes', 'Hospital Notes'),
    ('outpatient_cards', 'Outpatient Cards'),
    ('patient', 'Patient'),
    ('collateral_history',
     'Collateral History from relative/guardian'),
    (OTHER, 'Other'),
)

LP_REASON = (
    ('scheduled_per_protocol', 'Scheduled per protocol'),
    ('therapeutic_lp', 'Therapeutic LP'),
    ('clincal_deterioration', 'Clinical Deterioration'),
)

LOCATION_CARE = (
    ('government_healthcare', 'Government Healthcare'),
    ('private_healthcare', 'Private Healthcare'),
    ('ngo_healthcare', 'NGO Healthcare'),
    ('pharmacy', 'Pharmacy'),
    ('home', 'Home'),
    (OTHER, 'Other'),
)

MEDICINES = (
    ('fluconazole', 'Fluconazole'),
    ('amphotericin_b', 'Amphotericin B'),
    ('rifampicin', 'Rifampicin'),
    ('co_trimoxazole', 'Co-trimoxazole'),
    (OTHER, 'Other'),
)

PATIENT_TREATMENT_GROUP = (
    ('regimen_1',
     'Regimen 1 (Ambisome 10 mg/kg day 1 (single dose) +'
     ' fluconazole 1200mg/day + flucytosine 100mg/kg/day'
     ' for 14 days) '),
    ('regimen_2',
     'Regimen 2 (Amphotericin B 1 mg/kg + flucytocine 100mg/kg/day for 14 days) '),
)

POS_NEG_NA = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (NOT_APPLICABLE, 'Not applicable'),
)

PROTOCOL_VIOLATION = (
    ('failure_to_obtain_informed_consent', 'Failure to obtain informed '
     'consent'),
    ('enrollment_of_ineligible_patient', 'Enrollment of ineligible patient'),
    ('screening_procedure not done', 'Screening procedure required by '
     'protocol not done'),
    ('screening_or_on-study_procedure', 'Screening or on-study procedure/lab '
     'work required not done'),
    ('incorrect_research_treatment', 'Incorrect research treatment given to '
     'patient'),
    ('procedure_not_completed', 'On-study procedure required by protocol not '
     'completed'),
    ('visit_non-compliance', 'Visit non-compliance'),
    ('medication_stopped_early', 'Medication stopped early'),
    ('medication_noncompliance', 'Medication_noncompliance'),
    ('national_regulations_not_met', 'Standard WPD, ICH-GCP, local/national '
     'regulations not met'),
    (OTHER, 'Other'),
)


REASON_DRUG_MISSED = (
    ('toxicity', 'Toxicity'),
    ('missed', 'Missed'),
    ('refused', 'Refused'),
    ('not_required_acc_protocol', 'Not required according to protocol'),
    (OTHER, 'Other'),
)

REASON_STUDY_TERMINATED = (
    ('10_weeks_completed_followUp', 'Patient completed 10 weeks of follow-up'),
    ('patient_lost_to_follow_up', 'Patient lost to follow-up'),
    ('died', 'Reported/known to have died'),
    (CONSENT_WITHDRAWAL, 'Withdrawal of Subject Consent for '
     'participation'),
    ('care_transferred_to_another_institution', 'Care transferred to another '
                                                'institution'),
    ('late_exclusion_criteria_met', 'Late exclusion criteria met'),
    ('included_in_error', 'Included in error'),
)

REGIMEN = (
    ('single_dose', '1 (Single dose)'),
    ('two_doses', '2 (Two doses)'),
    ('three_doses', '3 (Three Doses)'),
    ('control', '4 (Control)'),
)

SIGNIFICANT_DX = (
    ('pulmonary_tb', 'Pulmonary TB'),
    ('extra_pulmonary_tb', 'Extra Pulmonary TB'),
    ('kaposi_sarcoma', 'Kaposi Sarcoma'),
    ('malaria', 'Malaria'),
    ('bacteraemia', 'Bacteraemia'),
    ('pneumonia', 'Pneumonia'),
    ('diarrhoeal_wasting', 'Diarrhoeal Wasting'),
    (OTHER, 'Other'),
)

STEROIDS_CHOICES = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('oral_prednisolone', 'Oral prednisolone'),
    ('iv_dexamethasone', 'IV Dexamethasone used'),
    (OTHER, 'Other'),
)

TB_SITE = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('pulmonary', 'Pulmonary'),
    ('extra_pulmonary', 'Extra pulmonary'),
    ('both', 'Both')
)

TB_SITE_DEATH = (
    ('meningitis', 'Meningitis'),
    ('pulmonary', 'Pulmonary'),
    ('disseminated', 'Disseminated'),
)

TRANSPORT = (
    ('bus', 'Bus'),
    ('train', 'Train'),
    ('ambulance', 'Ambulance'),
    ('private_taxi', 'Private Taxi'),
    ('hired_motorbike', 'Hired Motorbike'),
    ('own_car', 'Own Car'),
    ('own_motorbike', 'Own Motorbike'),
    ('bicycle', 'Bicycle'),
    ('foot', 'Foot'),
    (NOT_APPLICABLE, 'Not Applicable')
)

URINE_CULTURE_RESULTS_ORGANISM = (
    (NOT_APPLICABLE, 'Not Applicable'),
    ('e_coli', 'E.coli'),
    ('klebsiella_sp', 'Klebsiella sp.'),
    (OTHER, 'Other'),
)

VISIT_UNSCHEDULED_REASON = (
    ('patient_unwell_outpatient', 'Patient unwell (outpatient)'),
    ('recurrence_symptoms', 'Recurrence of symptoms'),
    ('raised_icp_management', 'Raised ICP Management'),
    ('art_initiation', 'ART initiation'),
    ('patient_hospitalised', 'Patient hospitalised'),
    (OTHER, 'Other'),
)

DAYS_MISSED = (
    (1, 'Day 1'), (2, 'Day 2'), (3, 'Day 3'), (4, 'Day 4'), (5, 'Day 5'),
    (6, 'Day 6'), (7, 'Day 7'), (8, 'Day 8'), (9, 'Day 9'), (10, 'Day 10'),
    (11, 'Day 11'), (12, 'Day 12'), (13, 'Day 13'), (14, 'Day 14'))

DOSES_MISSED = (
    (1, '1 Dose'), (2, '2 Doses'), (3, '3 Doses'), (4, '4 Doses'))

MG_MMOL_UNITS = (
    ('mg/dL', 'mg/dL'),
    ('mmol/L', 'mmol/L'),
)

MG_UMOL_UNITS = (
    ('mg/dL', 'mg/dL'),
    ('umol/L', 'μmol/L'),
)

MM3_PERC_UNITS = (
    ('mm3', 'mm3'),
    ('%', '%'),
    (NOT_APPLICABLE, 'Not Applicable'),
)

POS_NEG = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (IND, 'Indeterminate'),
    ('not_done', 'Not Done'),
)

RANKIN_SCORE = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('not done', 'Not done')
)

WEIGHT_DETERMINATION = (
    ('estimated', 'Estimated'),
    ('measured', 'Measured')
)

DEVIATION_VIOLATION = (
    (DEVIATION, 'Deviation'),
    (VIOLATION, 'Violation'),
)

VISIT_REASON = (
    (SCHEDULED, 'Scheduled'),
    (UNSCHEDULED, 'Not scheduled')
)

YES_NO = (
    (YES, 'Yes'),
    (NO, 'No'),
)

YES_NO_ND = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('not_done', 'Not Done'),
)

YES_NO_ALREADY_ND = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('already_on_rifampicin', 'Already on Rifampicin'),
    ('not_done', 'Not Done'),
)

YES_NO_ALREADY = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('already_on_rifampicin', 'Already on Rifampicin'),
)

YES_NO_ALREADY_ARV = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('on_arvs_before_enrollment', 'Already on ARVs before enrollment')
)

YES_NO_RESULTS_UNKNOWN = (
    (YES, YES),
    (NO, NO),
    (RESULTS_UNKNOWN, 'Results unknown'),
)

PREG_YES_NO_NA = (
    (YES, 'Yes'),
    (NO, 'No'),
    (NOT_APPLICABLE, 'Not Applicable: e.g. male, post-menopausal'),
)
