from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import AdverseEventForm
from ..models import AdverseEvent
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AdverseEvent, site=ambition_subject_admin)
class AdverseEventAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventForm

    radio_fields = {
        'ae_severity': admin.VERTICAL,
        'ae_intensity': admin.VERTICAL,
        'patient_treatment_group': admin.VERTICAL,
        'incident_study_relationship': admin.VERTICAL,
        'incident_drug_relationship_ambisome': admin.VERTICAL,
        'incident_drug_relationship_fluconozole': admin.VERTICAL,
        'other_ae_event_cause': admin.VERTICAL,
        'is_sae_event': admin.VERTICAL,
        'sae_event_reason': admin.VERTICAL,
        'is_susar': admin.VERTICAL,
        'susar_reported': admin.VERTICAL,
        'recurrence_cm_symptoms': admin.VERTICAL}

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
                'last_implicated_medication_administered_datetime',
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
                'susar_reported_datetime')},
         ),
        audit_fieldset_tuple
    )
