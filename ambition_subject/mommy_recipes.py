from dateutil.relativedelta import relativedelta
from faker import Faker
from faker.providers import BaseProvider
from model_mommy.recipe import Recipe, related, seq

from edc_base.utils import get_utcnow
from edc_base_test.faker import EdcBaseProvider
from edc_constants.constants import YES, POS, NEG, NO, UNKNOWN
from edc_visit_tracking.constants import SCHEDULED

from .models import (
    AdverseEvent, BloodResult, Death, Microbiology, FollowUp,
    ProtocolDeviationViolation, MissedVisit, PatientHistory, RecurrenceSymptom,
    SubjectScreening, SubjectRandomization, Week2, SubjectVisit, LumbarPunctureCsf,
    Radiology, StudyTerminationConclusion, SubjectLocator, SubjectConsent)
from .models.list_models import (
    Neurological, SignificantNewDiagnosis, MeningitisSymptom, Antibiotic)


class DateProvider(BaseProvider):

    def next_month(self):
        return (get_utcnow() + relativedelta(months=1)).date()

    def last_year(self):
        return (get_utcnow() - relativedelta(years=1)).date()

    def three_months_ago(self):
        return (get_utcnow() - relativedelta(months=3)).date()

    def thirty_four_weeks_ago(self):
        return (get_utcnow() - relativedelta(weeks=34)).date()

    def four_weeks_ago(self):
        return (get_utcnow() - relativedelta(weeks=4)).date()

    def yesterday(self):
        return (get_utcnow() - relativedelta(days=1)).date()


fake = Faker()
fake.add_provider(EdcBaseProvider)
fake.add_provider(DateProvider)

adverse_event = Recipe(
    AdverseEvent,
    ae_awareness_date=get_utcnow().date,
    description='life-threatening',
    ae_start_date=get_utcnow().date,
    ae_severity='death',
    ae_intensity='very high intensity',
    patient_treatment_group='inpatient',
    incident_study_relationship=YES,
    incident_drug_relationship_ambisome='Not related',
    incident_drug_relationship_fluconozole='Possibly related',
    last_implicated_medication_administered_datetime=get_utcnow,
    last_implicated_medication='ambisome',
    last_implicated_medication_dose='5g',
    last_implicated_medication_route='injection',
    other_ae_event_cause=YES,
    other_ae_event_cause_specify=None,
    action_taken_treatment='taken to hospital',
    recurrence_cm_symptoms=YES,
    is_sae_event=YES,
    sae_event_reason='Life-threatening',
    is_susar=YES,
    susar_reported=YES,
    susar_reported_datetime=get_utcnow(),
    ae_form_received_datetime=get_utcnow(),
    clinical_review_datetime=get_utcnow(),
    investigator_comments='good',
    ae_classification='disease associated with treatment',
    investigator_ae_description='caused death of a member of the family',
    regulatory_officials_notified_datetime=get_utcnow())

blood_result = Recipe(
    BloodResult,
    wbc=0.502,
    platelets=203,
    haemoglobin=0.54,
    absolute_neutrophil=1.02,
    creatinine=1.22,
    sodium=88,
    potassium=0.8,
    magnesium=0.088,
    total_bilirubin=0.9,
    alt=102,
    crp=0.89,
    urea=33,
    abs_cd4=59,
    proteinuria=YES,
    urine_cr_ag='Positive',
    are_results_normal=YES,
    abnormal_results_in_ae_range=YES)

death = Recipe(
    Death,
    study_day='Tuesday',
    death_as_inpatient=YES,
    cause_of_death_study_doctor_opinion='Cryptococcal meningitis',
    cause_other_study_doctor_opinion=None,
    cause_tb_study_doctor_opinion='Pulmonary',
    cause_of_death_tmg1_opinion='Cryptococcal meningitis',
    cause_other_tmg1_opinion=None,
    cause_tb_tmg1_opinion=None,
    cause_of_death_tmg2_opinion='Cryptococcal meningitis',
    cause_other_tmg2_opinion=None,
    cause_tb_tmg2_opinion=None,
    narrative_summary='adverse event resulted in death due to cryptococcal meningitis')

significant_new_diagnosis = Recipe(SignificantNewDiagnosis)

follow_up = Recipe(
    FollowUp,
    physical_symptoms=YES,
    headache=YES,
    visual_acuity_left_eye=0.5,
    visual_acuity_right_eye=0.85,
    glasgow_coma_score=8,
    confusion=YES,
    recent_seizure_less_72=NO,
    cn_palsy=NO,
    behaviour_change=YES,
    focal_neurology=YES,
    significant_new_diagnosis=related(significant_new_diagnosis),  # many2many
    other_significant_new_diagnosis=None,
    diagnosis_date=get_utcnow().date,
    fluconazole_dose='400mg daily',
    other_fluconazole_dose=None,
    is_rifampicin_started=YES,
    study_day_rifampicin_started=15,
    clinical_care_comments=None)

microbiology = Recipe(
    Microbiology,
    urine_culture_performed=YES,
    urine_culture_results='Positive',
    urine_culture_organism='Klebsiella sp.',
    urine_culture_organism_other=None,
    blood_culture_performed=YES,
    blood_culture_results='No growth',
    study_day_positive_blood_taken=55,
    blood_culture_organism='Mycobacterium Tuberculosis',
    blood_culture_organism_other=None,
    sputum_results_afb=POS,
    sputum_results_culture=NEG,
    sputum_result_genexpert=NEG,
    tissue_biopsy_taken=NO,
    study_day_positive_biopsy_taken=60,
    tissue_biopsy_organism='Cryptococcus neoformans')

missed_visit = Recipe(
    MissedVisit,
    missed_study_visit_date=get_utcnow,
    visit_missed=2,
    missed_visit_reason='Not feeling well',
    notes_or_action_taken='hospitalised')

neurological = Recipe(Neurological)

patient_history = Recipe(
    PatientHistory,
    symptom=None,
    headache_duration=2,
    visual_loss_duration=1,
    med_history=YES,
    tb_site='Pulmonary',
    tb_treatment=YES,
    taking_rifampicin=NO,
    rifampicin_started_date=get_utcnow().date,
    previous_infection=NO,
    infection_date=get_utcnow().date,
    taking_arv=NO,
    arvs=None,
    first_line_choice=None,
    patient_adherence=NO,
    last_dose=None,
    last_viral_load=None,
    temp=38,
    heart_rate=88,
    blood_pressure='120/80',
    respiratory_rate=22,
    weight=60,
    glasgow_coma_score=8,
    neurological=related(neurological),  # many2many
    neurological_other=None,
    focal_neurologic_deficit=None,
    visual_acuity_day=get_utcnow,
    left_acuity=0.52,
    right_acuity=0.53,
    lung_exam=YES,
    cryptococcal_lesions=NO,
    other_medications=NO,
    specify_medications=None)

protocol_deviation_violation = Recipe(
    ProtocolDeviationViolation,
    participant_safety_impact=NO,
    participant_safety_impact_details=None,
    study_outcomes_impact=NO,
    study_outcomes_impact_details=None,
    date_violation_datetime=get_utcnow(),
    protocol_violation_type='Failure to obtain informed consent',
    other_protocol_violation_type=None,
    violation_description=None,
    violation_reason=None,
    corrective_action_datetime=get_utcnow(),
    corrective_action=None,
    preventative_action_datetime=get_utcnow(),
    action_required='Participant to remain on trial')

meningitis_symptom = Recipe(MeningitisSymptom)

recurrence_symtom = Recipe(
    RecurrenceSymptom,
    meningitis_symptom=related(meningitis_symptom),
    meningitis_symptom_other=None,
    patient_readmitted=NO,
    glasgow_coma_score=8,
    recent_seizure=NO,
    behaviour_change=YES,
    confusion=YES,
    neurological=related(neurological),
    neurological_other=None,
    focal_neurologic_deficit=None,
    lp_completed=NO,
    amb_administered=NO,
    amb_duration=None,
    tb_treatment=YES,
    steroids_administered=NO,
    steroids_duration=None,
    steroids_choices=None,
    steroids_choices_other=None,
    CD4_count=50,
    antibiotic_treatment='Amoxicillin',
    antibiotic_treatment_other=None,
    on_arvs=NO,
    arv_date=None,
    arvs_stopped=NO,
    narrative_summary=None,
    dr_opinion='CM Relapse')

subject_screening = Recipe(
    SubjectScreening,
    sex='Male',
    age=40,
    meningitis_diagoses_by_csf_or_crag=YES,
    consent_to_hiv_test=YES,
    willing_to_give_informed_consent=YES,
    pregnancy_or_lactation=NO,
    previous_adverse_drug_reaction=NO,
    medication_contraindicated_with_study_drug=NO,
    two_days_amphotericin_b=NO,
    two_days_fluconazole=NO,
    is_eligible=True,
    ineligibility=None)

subject_randomization = Recipe(
    SubjectRandomization,
    hospital_admission_date=get_utcnow().date,
    inclusion_date=get_utcnow().date,
    abnormal_mental_status=NO,
    already_on_arvs=NO,
    arv_start_date=None,
    randomization_number='A(2)',
    consent_form_signed=YES,
    regimen=None)

antibiotic = Recipe(Antibiotic)

week2 = Recipe(
    Week2,
    discharged=NO,
    discharge_datetime=get_utcnow(),
    died=NO,
    death_datetime=get_utcnow(),
    ambisome_start_datetime=get_utcnow(),
    ambisome_stop_datetime=None,
    fluconazole_start_datetime=get_utcnow(),
    fluconazole_stop_datetime=None,
    drug_doses_missed=NO,
    ambisome_missed_doses=NO,
    ambisome_missed_reason='Administered acc to protocol',
    fluconazole_missed_doses=NO,
    fluconazole_missed_reason=None,
    other_drug=None,
    antibiotic=related(antibiotic),
    blood_receive=NO,
    units=None,
    hiv_status_pos=NO,
    new_hiv_diagnosis=UNKNOWN,
    clinic_assessment=NO,
    headache=YES,
    temperature=41.2,
    glasgow_coma_score=8,
    seizures_during_admission=NO,
    recent_seizure=NO,
    behaviour_change=YES,
    confusion=NO,
    cn_palsy=YES,
    focal_neurology=NO,
    weight=63,
    medicines='Fluconazole',
    significant_diagnosis='Extension to pain',
    glasgow_coma_score_eyes='Opens eyes spontaneously',
    glasgow_coma_score_verbal='Not Applicable',
    glasgow_coma_score_motor='Extension to pain')

subjectvisit = Recipe(
    SubjectVisit,
    reason=SCHEDULED,)

subject_locator = Recipe(
    SubjectLocator,
    alt_contact_cell_number='72200111',
    has_alt_contact=None,
    alt_contact_name=None,
    alt_contact_rel=None,
    alt_contact_cell=None,
    other_alt_contact_cell='760000111',
    alt_contact_tel=None)

study_termination_conclusion = Recipe(
    StudyTerminationConclusion,
    date_patient_terminated_study=25,
    last_research_termination_date=get_utcnow().date,
    last_research_termination_study_day=30,
    discharged_after_initial_admission=YES,
    initial_discharge_date=get_utcnow().date,
    initial_discharge_study_date=25,
    readmission_following_initial_discharge=YES,
    date_admitted=get_utcnow(),
    date_discharged=get_utcnow().date,
    study_termination_reason='Patient lost to follow-up',
    withdrawal_of_consent_reason=None,
    rifampicin_started_since_week4=NO,
    rifampicin_started_study_day=None,
    arv_regiment='AZT + 3TC + either ATZ/r or Lopinavir/r',
    is_naive=YES,
    date_started_arvs=get_utcnow(),
    date_switched_arvs=None,
    efv_or_nvp=None)

radiology = Recipe(
    Radiology,
    is_cxr_done=NO,
    cxr_type=None,
    infiltrate_location=None,
    cxr_description=None,
    is_ct_performed=NO,
    is_scanned_with_contrast=NO,
    brain_imaging_reason='New neurology',
    brain_imaging_reason_other=None,
    are_results_abnormal=NO,
    abnormal_results_reason=None,
    abnormal_results_reason_other=None,
    if_infarcts_location=None)

lumbar_puncture_csf = Recipe(
    LumbarPunctureCsf,
    reason_for_lp='Scheduled per protocol',
    opening_pressure=89,
    closing_pressure=70,
    csf_amount_removed=25,
    quantitative_culture=None,
    csf_culture=NO,
    other_csf_culture=None,
    csf_wbc_cell_count=200,
    differential_lymphocyte_count=300,
    differential_neutrophil_count=250,
    india_ink=POS,
    csf_glucose=1.9,
    csf_protein=200,
    csf_cr_ag=POS,
    csf_cr_ag_titres=300,
    csf_cr_ag_lfa=YES)

subject_consent = Recipe(
    SubjectConsent,
    subject_screening_reference=None,
    subject_identifier=None,
    study_site='40',
    consent_datetime=get_utcnow(),
    dob=fake.dob_for_consenting_adult,
    first_name=fake.first_name,
    last_name=fake.last_name,
    initials=fake.initials,
    gender='M',
    identity=seq('12315678'),
    confirm_identity=seq('12315678'),
    identity_type='OMANG',
    is_dob_estimated='-',)
