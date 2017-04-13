from model_mommy.recipe import Recipe
from .models import adverse_event, blood_results, death_report
from edc_base.utils import get_utcnow
from edc_constants.constants import YES


adverse_event = Recipe(
    adverse_event,
    ae_awareness_date=get_utcnow,
    description='life-threatening',
    ae_start_date=get_utcnow,
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
    susar_reported_datetime=get_utcnow,
    ae_form_received_datetime=get_utcnow,
    clinical_review_datetime=get_utcnow,
    investigator_comments='good',
    ae_classification='disease associated with treatment',
    investigator_ae_description='caused death of a member of the family',
    regulatory_officials_notified_datetime=get_utcnow)

blood_results = Recipe(
    blood_results,
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
    death_report,
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
