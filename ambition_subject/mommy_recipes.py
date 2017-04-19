from model_mommy.recipe import Recipe, related

from edc_base.utils import get_utcnow
from edc_constants.constants import YES, POS, NEG, NO

from .models import (
    AdverseEvent, BloodResult, DeathReport, Microbiology, FollowUp,
    ProtocolDeviationViolation, MissedVisit, PatientHistory, RecurrenceSymptom)
from .models.list_models import (
    Neurological, SignificantNewDiagnosis, MeningitisSymptom)


adverse_event = Recipe(
    AdverseEvent,
    ae_awareness_date=get_utcnow,
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

death_report = Recipe(
    DeathReport,
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
    meningitis_symptom=related(MeningitisSymptom),
    meningitis_symptom_other=None,
    patient_readmitted=NO,
    glasgow_coma_score=8,
    recent_seizure=NO,
    behaviour_change=YES,
    confusion=YES,
    neurological=related(Neurological),
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
