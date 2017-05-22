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
        'patient_group': admin.VERTICAL,
        'incident_study_relation': admin.VERTICAL,
        'ambisome_relation': admin.VERTICAL,
        'fluconozole_relation': admin.VERTICAL,
        'ae_cause_other': admin.VERTICAL,
        'is_sa_event': admin.VERTICAL,
        'sa_event_reason': admin.VERTICAL,
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
                'patient_group',
                'incident_study_relation',
                'ambisome_relation',
                'fluconozole_relation',
                'med_administered_datetime',
                'implicated_med',
                'implicated_med_dose',
                'implicated_med_route',
                'ae_cause_other',
                'ae_cause_other_specify',
                'action_taken',
                'recurrence_cm_symptoms',
                'is_sa_event',
                'sa_event_reason',
                'is_susar',
                'susar_reported',
                'susar_reported_datetime')},
         ),
        audit_fieldset_tuple
    )
