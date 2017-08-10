from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import PatientHistoryForm
from ..models import PatientHistory
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(PatientHistory, site=ambition_subject_admin)
class PatientHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = PatientHistoryForm

    filter_horizontal = ('neurological', 'symptom', 'specify_medications')

    radio_fields = {
        'med_history': admin.VERTICAL,
        'tb_site': admin.VERTICAL,
        'tb_treatment': admin.VERTICAL,
        'taking_rifampicin': admin.VERTICAL,
        'previous_infection': admin.VERTICAL,
        'new_hiv_diagnosis': admin.VERTICAL,
        'taking_arv': admin.VERTICAL,
        'arv_regimen': admin.VERTICAL,
        'first_line_choice': admin.VERTICAL,
        'patient_adherence': admin.VERTICAL,
        'ecog_score': admin.VERTICAL,
        'lung_exam': admin.VERTICAL,
        'cryptococcal_lesions': admin.VERTICAL,
        'vl_date_estimated': admin.VERTICAL,
        'cd4_date_estimated': admin.VERTICAL
    }

    fieldsets = (
        ('Current Symptoms', {
            'fields': [
                'subject_visit',
                'symptom',
                'headache_duration',
                'visual_loss_duration']}
         ),
        ('Previous Medical History', {
            'fields': [
                'med_history',
                'tb_site',
                'tb_treatment',
                'taking_rifampicin',
                'rifampicin_started_date', ]}
         ),
        ('Previous Opportunistic Infections', {
            'fields': [
                'previous_infection',
                'previous_infection_specify',
                'infection_date',
                'new_hiv_diagnosis',
                'taking_arv',
                'arv_date',
                'arv_regimen',
                'arv_regimen_other',
                'first_line_choice',
                'patient_adherence',
                'last_dose',
                'last_viral_load',
                'viral_load_date',
                'vl_date_estimated',
                'cd4_date',
                'cd4_date_estimated']}
         ),
        ('Vital Signs', {
            'fields': [
                'temp',
                'heart_rate',
                'blood_pressure',
                'respiratory_rate',
                'weight',
                'glasgow_coma_score']}
         ),
        ('Neurological', {
            'fields': [
                'neurological',
                'neurological_other',
                'focal_neurologic_deficit',
                'visual_acuity_day',
                'left_acuity',
                'right_acuity',
                'ecog_score']}
         ),
        ('Other', {
            'fields': [
                'lung_exam',
                'cryptococcal_lesions',
                'specify_medications',
                'specify_medications_other']}
         ), audit_fieldset_tuple)
