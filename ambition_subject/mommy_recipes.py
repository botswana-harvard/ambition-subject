from dateutil.relativedelta import relativedelta
from faker import Faker
from faker.providers import BaseProvider
from model_mommy.recipe import Recipe, related, seq

from edc_base.utils import get_utcnow
from edc_base_test.faker import EdcBaseProvider
from edc_constants.constants import NOT_APPLICABLE, YES, POS, NEG, NO
from edc_visit_tracking.constants import SCHEDULED

from .constants import A2
from .models import (
    AdverseEvent, AdverseEventTMG, BloodResult, Death, Microbiology, FollowUp,
    ProtocolDeviationViolation, MissedVisit, PatientHistory, RecurrenceSymptom,
    SubjectRandomization, Week2, SubjectVisit, LumbarPunctureCsf,
    Radiology, StudyTerminationConclusion, SubjectLocator, SubjectConsent)
from .models.list_models import (
    AEClassification, Neurological, SignificantNewDiagnosis, MeningitisSymptom,
    Antibiotic)


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

aeclassification = Recipe(AEClassification)

adverseevent = Recipe(
    AdverseEvent,
    ae_cause_other=NO,
    ae_cause_other_specify=None,
    is_sa_event=NO,
    is_susar=NO,
    susar_reported=NOT_APPLICABLE)

adverseeventtmg = Recipe(
    AdverseEventTMG)

bloodresult = Recipe(
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

significantnewdiagnosis = Recipe(SignificantNewDiagnosis)

followup = Recipe(
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
    significant_new_diagnosis=related(significantnewdiagnosis),  # many2many
    other_significant_new_diagnosis=None,
    diagnosis_date=get_utcnow().date,
    fluconazole_dose='400mg daily',
    other_fluconazole_dose=None,
    is_rifampicin_started=YES,
    study_day_rifampicin_started=15,
    clinical_care_comments=None)

subjectvisit = Recipe(
    SubjectVisit,
    reason=SCHEDULED,)

microbiology = Recipe(
    Microbiology,
    urine_culture_performed=NO,
    blood_culture_performed=NO,
    sputum_results_culture=NEG,
    tissue_biopsy_taken=NO,)

missedvisit = Recipe(
    MissedVisit,
    missed_study_visit_date=get_utcnow,
    visit_missed=2,
    missed_visit_reason='Not feeling well',
    notes_or_action_taken='hospitalised')

neurological = Recipe(Neurological)

patienthistory = Recipe(
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

protocoldeviationviolation = Recipe(
    ProtocolDeviationViolation)

meningitissymptom = Recipe(MeningitisSymptom)

recurrencesymtom = Recipe(
    RecurrenceSymptom,
    meningitis_symptom=related(meningitissymptom),
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

# subjectscreening = Recipe(
#     SubjectScreening,
#     gender='Male',
#     age_in_years=40,
#     meningitis_dx=YES,
#     will_hiv_test=YES,
#     pregnancy_or_lactation=NO,
#     previous_drug_reaction=NO,
#     contraindicated_meds=NO,
#     received_amphotericin=NO,
#     received_fluconazole=NO,
#     eligible=True,
#     reasons_ineligible=None)

subjectrandomization = Recipe(
    SubjectRandomization,
    hospital_admission_date=get_utcnow().date,
    abnormal_mental_status=NO,
    on_arvs=NO,
    arv_start_date=None,
    rando_category=A2,
    regimen=None)

antibiotic = Recipe(Antibiotic)

week2 = Recipe(
    Week2,
    discharged=NO,
    died=NO,
    flucon_start_datetime=get_utcnow(),
    flucon_stop_datetime=None,
    other_drug=None,
    antibiotic=related(antibiotic),
    blood_received=NO,
    units=None,
    headache=YES,
    temperature=41.2,
    glasgow_cs=8,
    seizures_during_admission=NO,
    recent_seizure=NO,
    behaviour_change=YES,
    confusion=NO,
    cn_palsy=YES,
    focal_neurology=NO,
    medicines='Fluconazole',)

subjectlocator = Recipe(
    SubjectLocator,
    alt_contact_cell_number='72200111',
    has_alt_contact=None,
    alt_contact_name=None,
    alt_contact_rel=None,
    alt_contact_cell=None,
    other_alt_contact_cell='760000111',
    alt_contact_tel=None)

studyterminationconclusion = Recipe(
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
    arv_regimen='AZT + 3TC + either ATZ/r or Lopinavir/r',
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

lumbarpuncturecsf = Recipe(
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

subjectconsent = Recipe(
    SubjectConsent,
    subject_screening=None,
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
