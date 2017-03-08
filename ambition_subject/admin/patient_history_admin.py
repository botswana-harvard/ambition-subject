from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import PatientHistoryForm
from ..models import PatientHistory
from .modeladmin_mixins import ModelAdminMixin


@admin.register(PatientHistory, site=ambition_subject_admin)
class PatientHistoryAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = PatientHistoryForm

    filter_horizontal = ('current_symptoms', 'neurological')

    radio_fields = {
        'med_history': admin.VERTICAL,
        'tb_site': admin.VERTICAL,
        'tb_treatment': admin.VERTICAL,
        'taking_rifampicin': admin.VERTICAL,
        'previous_infection': admin.VERTICAL,
        'taking_arv': admin.VERTICAL,
        'arvs': admin.VERTICAL,
        'first_line_choice': admin.VERTICAL,
        'patient_adherence': admin.VERTICAL,
        'lung_exam': admin.VERTICAL,
        'cryptococcal_lesions': admin.VERTICAL,
        'other_medications': admin.VERTICAL,
    }

    fieldsets = (
        ('Current Symptoms', {
            'fields': (
                'current_symptoms',
                'headache_duration',
                'visual_loss_duration')}
         ),
        ('Previous Medical History', {
            'fields': (
                'med_history',
                'tb_site',
                'tb_treatment',
                'taking_rifampicin',
                'rifampicin_started_date',
                'previous_infection',
                'infection_date',
                'taking_arv',
                'arv_date',
                'arvs',
                'first_line_choice',
                'patient_adherence',
                'last_dose',
                'last_viral_load')}
         ),
        ('Vital Signs', {
            'fields': (
                'temp',
                'heart_rate',
                'blood_pressure',
                'respiratory_rate',
                'weight',
                'glasgow_coma_score')}
         ),
        ('Neurological', {
            'fields': (
                'neurological',
                'neurological_other',
                'focal_neurologic_deficit',
                'visual_acuity_day',
                'left_acuity',
                'right_acuity')}
         ),
        ('Other', {
            'fields': (
                'lung_exam',
                'cryptococcal_lesions',
                'other_medications',
                'other_medications_other')}
         ), audit_fieldset_tuple)
