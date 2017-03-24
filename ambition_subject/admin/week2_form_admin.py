from django.contrib import admin

from ..admin_site import ambition_subject_admin
from ..forms import Week2Form
from .modeladmin_mixins import ModelAdminMixin
from ..models import Week2
from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fieldset_tuple


@admin.register(Week2, site=ambition_subject_admin)
class Week2Admin(ModelAdminMixin, admin.ModelAdmin):

    form = Week2Form

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
                'AmBisome_start_datetime',
                'AmBisome_stop_datetime',
                'Fluconazole_start_datetime',
                'Fluconazole_stop_datetime',
                'drug_doses_missed',
                'AmBisome_missed_doses',
                'AmBisome_missed_reason',
                'Fluconazole_missed_doses',
                'Fluconazole_missed_reason',
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
                'signifiant_diagnosis')}
         ],
        ['Glasgow Coma Score', {
            'fields': (
                'glasgow_coma_score_eyes',
                'glasgow_coma_score_verbal',
                'glasgow_coma_score_motor')}],
        audit_fieldset_tuple
    )
