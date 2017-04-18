from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import FollowUpForm
from ..models import FollowUp
from .modeladmin_mixins import ModelAdminMixin


@admin.register(FollowUp, site=ambition_subject_admin)
class FollowUpAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = FollowUpForm

    radio_fields = {
        'physical_symptoms': admin.VERTICAL,
        'headache': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'recent_seizure_less_72': admin.VERTICAL,
        'cn_palsy': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'focal_neurology': admin.VERTICAL,
        'fluconazole_dose': admin.VERTICAL,
        'is_rifampicin_started': admin.VERTICAL}

    fieldsets = (
        ('Clinical Assessment', {
            'fields': (
                'physical_symptoms',
                'headache',
                'visual_acuity_left_eye',
                'visual_acuity_right_eye',
                'glasgow_coma_score',
                'confusion',
                'recent_seizure_less_72',
                'cn_palsy',
                'behaviour_change',
                'focal_neurology')},
         ),
        ('Drug Treatment', {
            'fields': (
                'other_significant_new_diagnosis',
                'diagnosis_date',
                'fluconazole_dose',
                'other_fluconazole_dose',
                'is_rifampicin_started',
                'study_day_rifampicin_started',
                'clinical_care_comments')}),
        audit_fieldset_tuple
    )
