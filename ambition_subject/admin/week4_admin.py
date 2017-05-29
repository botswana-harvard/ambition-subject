from django.contrib import admin

from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import Week4Form
from ..models import Week4

from .modeladmin_mixins import ModelAdminMixin


@admin.register(Week4, site=ambition_subject_admin)
class Week4Admin(ModelAdminMixin, admin.ModelAdmin):

    form = Week4Form

    fieldsets = (
        ['Clinical Assessment', {
            'fields': (
                'subject_visit',
                'physical_symptoms',
                'headache',
                'visual_acuity_left_eye',
                'visual_acuity_right_eye',
                'glasgow_coma_score',
                'confusion',
                'recent_seizure_less_72',
                'cn_palsy',
                'behaviour_change',
                'focal_neurology',
                'significant_new_diagnosis',
                'other_significant_new_diagnosis',
                'diagnosis_date'
            )}
         ],
        audit_fieldset_tuple
    )

    radio_fields = {
        'physical_symptoms': admin.VERTICAL,
        'headache': admin.VERTICAL,
        'recent_seizure_less_72': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'cn_palsy': admin.VERTICAL,
        'focal_neurology': admin.VERTICAL,
    }
