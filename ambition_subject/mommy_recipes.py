from dateutil.relativedelta import relativedelta
from faker import Faker
from faker.providers import BaseProvider
from model_mommy.recipe import Recipe, related, seq

from edc_base.utils import get_utcnow
from edc_base_test.faker import EdcBaseProvider
from edc_constants.constants import NOT_APPLICABLE, YES, NEG, NO, OTHER
from edc_visit_tracking.constants import SCHEDULED

from .constants import A2
from .models import (
    AdverseEvent, AdverseEventTMG, AdverseEventFollowUp, BloodResult, Death, Microbiology, FollowUp,
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
    ae_study_relation_possibility=YES,
    ambisome_relation='not_related',
    fluconazole_relation='not_related',
    amphotericin_b_relation='not_related',
    ae_cause=NO,
    ae_cause_other=None)

adverseeventtmg = Recipe(
    AdverseEventTMG)

bloodresult = Recipe(
    BloodResult,
    wbc=200,
    platelets=203,
    haemoglobin=222,
    absolute_neutrophil=1.02,
    creatinine=1.22,
    sodium=88,
    potassium=0.8,
    magnesium=5,
    total_bilirubin=0.9,
    alt=102,
    crp=200,
    urea=33,
    abs_cd4=59,
    proteinuria=YES,
    urine_cr_ag='POS',
    are_results_normal=YES,
    abnormal_results_in_ae_range=YES)

death = Recipe(
    Death,
    study_day=1,
    death_as_inpatient=YES,
    cause_of_death_study_doctor_opinion='art_toxicity',
    cause_other_study_doctor_opinion='None',
    cause_tb_study_doctor_opinion=None,
    cause_of_death_tmg1_opinion='art_toxicity',
    cause_other_tmg1_opinion='None',
    cause_tb_tmg1_opinion=None,
    cause_of_death_tmg2_opinion='art_toxicity',
    cause_other_tmg2_opinion='None',
    cause_tb_tmg2_opinion=None,
    narrative_summary='adverse event resulted in death due to cryptococcal meningitis')


significantnewdiagnosis = Recipe(
    SignificantNewDiagnosis,
    name=NOT_APPLICABLE,
    short_name=NOT_APPLICABLE
)

followup = Recipe(
    FollowUp,
    physical_symptoms=NO,
    headache=NO,
    glasgow_coma_score=8,
    confusion=NO,
    cn_palsy=NO,
    tb_pulmonary_dx=NO,
    extra_pulmonary_tb_dx=NO,
    kaposi_sarcoma_dx=NO,
    malaria_dx=NO,
    bacteraemia_dx=NO,
    pneumonia_dx=NO,
    diarrhoeal_wasting_dx=NO,
    behaviour_change=NO,
    focal_neurology=NO,
    fluconazole_dose='800mg_daily',
    rifampicin_started=NO)

adverseeventfollowup = Recipe(
    AdverseEventFollowUp,
    relevant_history=None,
    med_name_given=None,
    med_given_dosage=None,
    med_given_indication=None,
    work_up=None,
    treatment_plan=None,
    treated=None)

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

meningitissymptom = Recipe(
    MeningitisSymptom,
    name=OTHER,
    short_name='Other'
)

neurological = Recipe(
    Neurological,
    name='meningismus',
    short_name='Meningismus'
)

recurrencesymptom = Recipe(
    RecurrenceSymptom,
    meningitis_symptom=[meningitissymptom],
    meningitis_symptom_other=None,
    patient_readmitted=NO,
    glasgow_coma_score=8,
    recent_seizure=NO,
    behaviour_change=YES,
    confusion=YES,
    neurological=[neurological],
    focal_neurologic_deficit=None,
    lp_completed=NO,
    amb_administered=NO,
    amb_duration=1,
    tb_treatment=YES,
    steroids_administered=NO,
    steroids_duration=None,
    steroids_choices='oral_prednisolone',
    steroids_choices_other=None,
    CD4_count=50,
    antibiotic_treatment=None,
    antibiotic_treatment_other=None,
    on_arvs=NO,
    arv_date=None,
    arvs_stopped=NO,
    narrative_summary='description',
    dr_opinion='cm_release')

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
    when_cxr_done=None,
    cxr_type=NOT_APPLICABLE,
    infiltrate_location=NOT_APPLICABLE,
    cxr_description=None,
    is_ct_performed=YES,
    date_ct_performed=get_utcnow(),
    is_scanned_with_contrast=NO,
    brain_imaging_reason='reduction_in_gcs',
    brain_imaging_reason_other=None,
    are_results_abnormal=NOT_APPLICABLE,
    abnormal_results_reason=NOT_APPLICABLE,
    abnormal_results_reason_other=NOT_APPLICABLE,
    if_infarcts_location=None)

lumbarpuncturecsf = Recipe(
    LumbarPunctureCsf,
    csf_culture=NO,
    opening_pressure=15,
    csf_amount_removed=5,
    csf_wbc_cell_count=250,
    differential_lymphocyte_count=250,
    differential_neutrophil_count=250,
    csf_protein=10)

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
