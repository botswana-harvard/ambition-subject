from django.contrib import admin

from ..admin_site import ambition_subject_admin
from ..forms import Week2Form
from .modeladmin_mixins import ModelAdminMixin
from ..models import Week2
from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fieldset_tuple


@admin.register(Week2, site=ambition_subject_admin)
class Week2Admin(ModelAdminMixin, admin.ModelAdmin):

    form = Week2Form

    filter_horizontal = ('other_drug_type', 'antibiotic_list',)

    fieldsets = (
        ['Admission history', {
            'fields': (
                'discharged',
                'discharge_datetime',
                'died',
                'death_datetime')},
         ],
        ['Induction phase Study medication', {
            'fields': (
                'ambisome_start_datetime',
                'ambisome_stop_datetime',
                'fluconazole_start_datetime',
                'fluconazole_stop_datetime',
                'drug_doses_missed',
                'ambisome_missed_doses',
                'ambisome_missed_reason',
                'fluconazole_missed_doses',
                'fluconazole_missed_reason',
                'other_drug_type',
                'antibiotic_list',
                'blood_received',
                'units',
                'hiv_status_pos',
                'new_hiv_diagnosis')}
         ],
        ['Clinical Assessment', {
            'fields': (
                'clinic_assessment',
                'headache',
                'temperature',
                'glasgow_coma_score',
                'seizures_during_admission',
                'recent_seizure',
                'behaviour_change',
                'confusion',
                'cn_palsy',
                'focal_neurology',
                'weight',
                'medicines',
                'significant_diagnosis')}
         ],
        ['Glasgow Coma Score', {
            'fields': (
                'glasgow_coma_score_eyes',
                'glasgow_coma_score_verbal',
                'glasgow_coma_score_motor')}],
        audit_fieldset_tuple
    )

    radio_fields = {
        'discharged': admin.VERTICAL,
        'died': admin.VERTICAL,
        'drug_doses_missed': admin.VERTICAL,
        'ambisome_missed_reason': admin.VERTICAL,
        'fluconazole_missed_doses': admin.VERTICAL,
        'fluconazole_missed_reason': admin.VERTICAL,
        'blood_received': admin.VERTICAL,
        'blood_received': admin.VERTICAL,
        'hiv_status_pos': admin.VERTICAL,
        'new_hiv_diagnosis': admin.VERTICAL,
        'clinic_assessment': admin.VERTICAL,
        'headache': admin.VERTICAL,
        'seizures_during_admission': admin.VERTICAL,
        'recent_seizure': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'cn_palsy': admin.VERTICAL,
        'focal_neurology': admin.VERTICAL,
        'medicines': admin.VERTICAL,
        'significant_diagnosis': admin.VERTICAL,
        'glasgow_coma_score_eyes': admin.VERTICAL,
        'glasgow_coma_score_verbal': admin.VERTICAL,
        'glasgow_coma_score_motor': admin.VERTICAL
    }
