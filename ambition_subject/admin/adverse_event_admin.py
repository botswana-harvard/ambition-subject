from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import AdverseEventForm
from ..models import AdverseEvent
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AdverseEvent, site=ambition_subject_admin)
class AdverseEventAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventForm

    fieldsets = (
        (None, {
            'fields': (
                'ae_identifier',
                'subject_identifier',
                'regimen',
                'report_datetime',
                'ae_description',
                'ae_awareness_date',
                'ae_start_date',
                'ae_severity_grade',
                'ae_intensity',
                'ae_study_relation_possibility',
                'ambisome_relation',
                'fluconazole_relation',
                'amphotericin_b_relation',
                'flucytosine_relation',
                'details_last_study_drug',
                'med_administered_datetime',
                'ae_cause',
                'ae_cause_other',
                'ae_treatment',
                'ae_cm_recurrence',
                'sa_event',
                'sae_possibility',
                'susar_possility',
                'susar_reported',
                'susar_reported_datetime')},
         ),
        audit_fieldset_tuple
    )

    radio_fields = {
        'ae_severity_grade': admin.VERTICAL,
        'ae_intensity': admin.VERTICAL,
        'ae_study_relation_possibility': admin.VERTICAL,
        'ambisome_relation': admin.VERTICAL,
        'fluconazole_relation': admin.VERTICAL,
        'amphotericin_b_relation': admin.VERTICAL,
        'flucytosine_relation': admin.VERTICAL,
        'ae_cause': admin.VERTICAL,
        'ae_cm_recurrence': admin.VERTICAL,
        'sa_event': admin.VERTICAL,
        'sae_possibility': admin.VERTICAL,
        'susar_possility': admin.VERTICAL,
        'susar_reported': admin.VERTICAL}

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj=obj)
        return fields + ('ae_identifier', )
