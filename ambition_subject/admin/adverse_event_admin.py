from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import AdverseEventForm
from ..models import AdverseEvent


@admin.register(AdverseEvent, site=ambition_subject_admin)
class AdverseEventAdmin(admin.ModelAdmin):

    form = AdverseEventForm

    fieldsets = (
        ('Initial Report', {
            'fields': (
                'ae_awareness_date',
                'description',
                'ae_start_date',
                'ae_severity',
                'ae_intensity',
                'patient_treatment_group',
                'incident_study_relationship',
                'incident_drug_relationship_ambisome',
                'incident_drug_relationship_fluconozole',
                'last_implicated_medication_administered_on',
                'last_implicated_medication',
                'last_implicated_medication_dose',
                'last_implicated_medication_route',
                'other_ae_event_cause',
                'other_ae_event_cause_specify',
                'action_taken_treatment',
                'recurrence_cm_symptoms',
                'is_sae_event',
                'sae_event_reason',
                'is_susar',
                'susar_reported',
                'susar_reported_on',
                '')},
         ),
        ('For completion by TMG Investigator Only', {
            'fields': (
                'ae_form_received_on',
                'clinical_review_on',
                'investigator_comments',
                'investigator_ae_description',
                'ae_classification',
                'regulatory_officials_notified_on')}),
        audit_fieldset_tuple,
    )
