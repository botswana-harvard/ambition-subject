from ambition_rando.constants import SINGLE_DOSE, CONTROL
from ambition_validators import WORKING, NO_GROWTH, KLEBSIELLA_SPP
from ambition_validators import CRYPTOCOCCUS_NEOFORMANS, BACTERIA
from edc_constants.constants import NEG, OTHER, POS, NOT_APPLICABLE, NOT_DONE
from edc_constants.constants import NORMAL, IND, YES, NO, UNKNOWN
from edc_reportable import MILLIGRAMS_PER_DECILITER, MILLIMOLES_PER_LITER, MICROMOLES_PER_LITER
from edc_reportable import GRADE3, GRADE4, MICROMOLES_PER_LITER_DISPLAY, MM3, MM3_DISPLAY
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED

from .constants import AZT_3TC_with_ATZ_r_or_Lopinavir_r
from .constants import AZT_3TC_with_EFV_NVP_or_DTG, DEAD
from .constants import CONSENT_WITHDRAWAL, ROUTINE_APPT, THREE_DOSES, TWO_DOSES
from .constants import DEVIATION, VIOLATION, TUBERCULOSIS, RESULTS_UNKNOWN
from .constants import ECOLI, TDF_3TC_FTC_with_EFV_or_NVP
from .constants import TDF_3TC_FTC_with_ATZ_r_or_Lopinavir_r


ABNORMAL_RESULTS_REASON = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('cerebral_oedema', 'Cerebral oedema'),
    ('hydrocephalus', 'Hydrocephalus'),
    ('cryptococcomus', 'Cryptococcomus'),
    ('dilated_virchow_robin_spaces', 'Dilated Virchow-Robin spaces'),
    ('enhancing_mass_lesions',
     'Enhancing mass lesions DD Toxoplasmosis, TB, Lymphoma'),
    ('infarcts', 'Infarcts'),
    (OTHER, 'Other'))

ACTION_REQUIRED = (
    ('remain_on_study', 'Participant to remain on trial'),
    ('to_be_withdrawn', 'Participant to be withdrawn from trial'),
    ('remain_on_study_modified',
     'Patient remains on study but data analysis will be modified')
)

ACTIVITIES_MISSED = (
    (WORKING, 'Working'),
    ('studying', 'Studying'),
    ('caring_for_children', 'Caring for children'),
    ('maintaining_house', 'Maintaining the house'),
    ('nothing', 'Nothing'),
    (OTHER, 'Other'),
)


ANTIBIOTICS = (
    ('amoxicillin', 'Amoxicillin'),
    ('doxycycline', 'Doxycycline'),
    ('flucloxacillin', 'Flucloxacillin'),
    ('ceftriaxone', 'Ceftriaxone'),
    ('erythromycin',
     'Erythromycin (contra-indicated with concomitant high dose Fluconazole)'),
    ('ciprofloxacin',
     'Ciprofloxacin (avoid with concomitant high dose Fluconazole)'),
    (OTHER, 'Other'),
)

APPOINTMENT_REASON = (
    (ROUTINE_APPT, 'Routine'),
    (UNSCHEDULED, 'Unscheduled'),
)
ARV_REGIMEN = (
    (NOT_APPLICABLE, 'Not applicable'),
    (TDF_3TC_FTC_with_EFV_or_NVP,
     'TDF + 3TC/FTC + either EFV or NVP or DTG'),
    (AZT_3TC_with_EFV_NVP_or_DTG,
     'AZT + 3TC + either EFV or NVP or DTG'),
    (TDF_3TC_FTC_with_ATZ_r_or_Lopinavir_r,
     'TDF + 3TC/FTC + either ATZ/r or Lopinavir/r'),
    (AZT_3TC_with_ATZ_r_or_Lopinavir_r,
     'AZT + 3TC + either ATZ/r or Lopinavir/r'),
    (OTHER, 'Other'),
)

FIRST_ARV_REGIMEN = (
    (NOT_APPLICABLE, 'Not applicable'),
    (TDF_3TC_FTC_with_EFV_or_NVP,
     'TDF + 3TC/FTC + either EFV or NVP or DTG'),
    (AZT_3TC_with_EFV_NVP_or_DTG,
     'AZT+3TC+ either EFV or NVP or DTG'),
    (OTHER, 'Other'),
)

SECOND_ARV_REGIMEN = (
    (NOT_APPLICABLE, 'Not applicable'),
    (TDF_3TC_FTC_with_ATZ_r_or_Lopinavir_r,
     'TDF + 3TC/FTC + either ATZ/r or Lopinavir/r'),
    (AZT_3TC_with_ATZ_r_or_Lopinavir_r,
     'AZT +3TC + either ATZ/r or Lopinavir/r'),
    (OTHER, 'Other'),
)

BLOOD_CULTURE_RESULTS_ORGANISM = (
    (NOT_APPLICABLE, 'Not applicable'),
    (CRYPTOCOCCUS_NEOFORMANS, 'Cryptococcus neoformans'),
    (BACTERIA, 'Bacteria'),
    ('bacteria_and_cryptococcus', 'Bacteria and Cryptococcus'),
    (OTHER, 'Other'),
)

BIOPSY_RESULTS_ORGANISM = (
    (NOT_APPLICABLE, 'Not applicable'),
    (CRYPTOCOCCUS_NEOFORMANS, 'Cryptococcus neoformans'),
    ('mycobacterium_tuberculosis', 'Mycobacterium Tuberculosis'),
    (OTHER, 'Other'),
)

BACTERIA_TYPE = (
    (NOT_APPLICABLE, 'Not applicable'),
    (ECOLI, 'E.coli'),
    (KLEBSIELLA_SPP, 'Klebsiella spp.'),
    ('streptococcus_pneumoniae', 'Streptococcus pneumoniae'),
    ('staphylococus_aureus', '(Sensitive) Staphylococus aureus'),
    ('mrsa', 'MRSA'),
    (OTHER, 'Other'),
)

BRAIN_IMAGINING_REASON = (
    (NOT_APPLICABLE, 'Not applicable'),
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
    ('3', 'III'),
    ('6', 'VI'),
    ('7', 'VII'),
    ('8', 'VIII'),
)

CLINICAL_ASSESSMENT = (
    (NOT_APPLICABLE, 'Not applicable'),
)

CULTURE_RESULTS = (
    (NOT_APPLICABLE, 'Not applicable'),
    (NO_GROWTH, 'No growth'),
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
    (NOT_APPLICABLE, 'Not applicable'),
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
    ('2', 'Ambulatory and capable of all self-care but unable to carry out '
     'any work activities; up and about more than 50% of waking hours '),
    ('3', 'Capable of only limited self-care; confined to bed or chair more than '
     '50% of waking hours'),
    ('4',
     'Completely disabled; cannot carry on any self-care; totally confined to bed or chair'),
    ('5', 'Deceased'),
)

FIRST_LINE_REGIMEN = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('EFV', 'EFV'),
    ('DTG', 'DTG'),
    ('NVP', 'NVP'),
)

FLUCONAZOLE_DOSE = (
    ('800mg_daily', '800mg daily'),
    (OTHER, 'Other'),
    (NOT_DONE, 'Not done'),
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
    (NOT_APPLICABLE, 'Not applicable'),
)

GLASGOW_COMA_SCORE_VERBAL = (
    ('makes_no_sounds', 'Makes no sounds'),
    ('makes_sounds', 'Makes sounds'),
    ('makes_words', 'Makes words'),
    ('disoriented', 'Disoriented'),
    ('oriented', 'Oriented'),
    (NOT_APPLICABLE, 'Not applicable'),
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
    ('country_id', 'Country ID number'),
    ('drivers', 'Driver\'s license'),
    ('passport', 'Passport'),
    ('hospital_no', 'Hospital number'),
    ('country_id_rcpt', 'Country ID receipt'),
    (OTHER, 'Other'),
)


INFECTION = (
    ('kaposi_sarcoma', 'Kaposi Sarcoma'),
    ('herpes_zoster_virus', 'Herpes-Zoster virus'),
    ('oesophageal_candidiasis', 'Oesophageal Candidiasis'),
    ('PCP', 'PCP'),
    ('cytomegalovirus', 'Cytomegalovirus'),
    (OTHER, 'Other')
)


INFILTRATE_LOCATION = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('lul', 'LUL'),
    ('lll', 'LLL'),
    ('rul', 'RUL'),
    ('rll', 'RLL'),
    ('rml', 'RML'),
    ('diffuse', 'Diffuse'),
)

INFO_SOURCE = (
    ('hospital_notes', 'Hospital notes'),
    ('outpatient_cards', 'Outpatient cards'),
    ('patient', 'Patient'),
    ('collateral_history',
     'Collateral History from relative/guardian'),
    (OTHER, 'Other'),
)

LP_REASON = (
    ('scheduled_per_protocol', 'Scheduled per protocol'),
    ('therapeutic_lp', 'Therapeutic LP'),
    ('clincal_deterioration', 'Clinical deterioration'),
)

LOCATION_CARE = (
    ('government_healthcare', 'Government healthcare'),
    ('private_healthcare', 'Private healthcare'),
    ('ngo_healthcare', 'NGO healthcare'),
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
    ('not_required', 'Not required according to protocol'),
    (OTHER, 'Other'),
)

REASON_STUDY_TERMINATED = (
    ('10_weeks_completed_follow_up',
     'Patient completed 10 weeks of follow-up'),
    ('patient_lost_to_follow_up', 'Patient lost to follow-up'),
    (DEAD, 'Reported/known to have died'),
    (CONSENT_WITHDRAWAL, 'Withdrawal of Subject Consent for '
     'participation'),
    ('care_transferred_to_another_institution',
     'Care transferred to another institution'),
    ('late_exclusion_criteria_met', 'Late exclusion criteria met'),
    ('included_in_error', 'Included in error'),
)

REGIMEN = (
    (SINGLE_DOSE, '1 (single dose)'),
    (TWO_DOSES, '2 (two doses)'),
    (THREE_DOSES, '3 (three Doses)'),
    (CONTROL, '4 (control)'),
)

REPORTABLE = (
    (NOT_APPLICABLE, 'Not applicable'),
    (NO, 'No'),
    (GRADE3, 'Grade 3'),
    (GRADE4, 'Grade 4'),
)

SIGNIFICANT_DX = (
    ('pulmonary_tb', 'Pulmonary TB'),
    ('extra_pulmonary_tb', 'Extra-pulmonary TB'),
    ('kaposi_sarcoma', 'Kaposi-sarcoma'),
    ('malaria', 'Malaria'),
    ('bacteraemia', 'Bacteraemia'),
    ('pneumonia', 'Pneumonia'),
    ('diarrhoeal_wasting', 'Diarrhoeal wasting'),
    (OTHER, 'Other'),
)

STEROIDS_CHOICES = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('oral_prednisolone', 'Oral Prednisolone'),
    ('iv_dexamethasone', 'IV Dexamethasone used'),
    (OTHER, 'Other'),
)

TB_SITE = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('pulmonary', 'Pulmonary'),
    ('extra_pulmonary', 'Extra-pulmonary'),
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
    ('private_taxi', 'Private taxi'),
    ('hired_motorbike', 'Hired motorbike'),
    ('own_car', 'Own car'),
    ('own_motorbike', 'Own motorbike'),
    ('bicycle', 'Bicycle'),
    ('foot', 'Foot'),
    (NOT_APPLICABLE, 'Not applicable')
)

URINE_CULTURE_RESULTS_ORGANISM = (
    (NOT_APPLICABLE, 'Not applicable'),
    (ECOLI, 'E.coli'),
    (KLEBSIELLA_SPP, 'Klebsiella spp.'),
    (OTHER, 'Other'),
)

VISIT_UNSCHEDULED_REASON = (
    ('patient_unwell_outpatient', 'Patient unwell (outpatient)'),
    ('recurrence_symptoms', 'Recurrence of symptoms'),
    ('raised_icp_management', 'Raised ICP management'),
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
    (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
    (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
)

MG_UMOL_UNITS = (
    (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
    (MICROMOLES_PER_LITER, MICROMOLES_PER_LITER_DISPLAY),
)

MM3_PERC_UNITS = (
    (MM3, MM3_DISPLAY),
    ('%', '%'),
    (NOT_APPLICABLE, 'Not applicable'),
)

POS_NEG = (
    (POS, 'Positive'),
    (NEG, 'Negative'),
    (IND, 'Indeterminate'),
    (NOT_DONE, 'Not done'),
)

RANKIN_SCORE = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    (NOT_DONE, 'Not done')
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
    (NOT_DONE, 'Not done'),
)

YES_NO_ALREADY_ND = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('already_on_rifampicin', 'Already on Rifampicin'),
    (NOT_DONE, 'Not done'),
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

PATIENT_REL = (
    ('patient', 'Patient'),
    ('next_of_kin', 'Next of Kin/Relative'),
)
