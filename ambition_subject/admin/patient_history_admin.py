from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import PatientHistoryForm
from ..models import PatientHistory
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(PatientHistory, site=ambition_subject_admin)
class PatientHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = PatientHistoryForm

    filter_horizontal = ('neurological', 'symptom', 'specify_medications',
                         'previous_non_tb_oi')

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
                'tb_history',
                'tb_site',
                'tb_treatment',
                'taking_rifampicin',
                'rifampicin_started_date', ]}
         ),
        ('Previous Opportunistic Infections', {
            'fields': [
                'previous_non_tb_oi',
                'previous_non_tb_oi_other',
                #                 'previous_non_tb_oi_date',
                'new_hiv_diagnosis',
                'taking_arv',
                'arv_date',
                'first_arv_regimen',
                'first_arv_regimen_other',
                'second_arv_regimen',
                'second_arv_regimen_other',
                'first_line_choice',
                'patient_adherence',
                'last_dose',
                'last_viral_load',
                'viral_load_date',
                'vl_date_estimated',
                'last_cd4',
                'cd4_date',
                'cd4_date_estimated']}
         ),
        ('Vital Signs', {
            'fields': [
                'temp',
                'heart_rate',
                'sys_blood_pressure',
                'dia_blood_pressure',
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
         ),

        ('Medical Expenses', {
            'fields': [
                'personal_he_spend',
                'proxy_he_spend',
                'he_spend_last_4weeks',
                'care_before_hospital',
                'location_care',
                'location_care_other',
                'transport_form',
                'transport_cost',
                'transport_duration',
                'care_provider',
                'care_provider_other',
                'paid_treatment',
                'paid_treatment_amount',
                'medication_bought',
                'medication_payment',
                'other_place_visited',
                'duration_present_condition',
                'activities_missed',
                'activities_missed_other',
                'time_off_work',
                'carer_time_off',
                'loss_of_earnings',
                'earnings_lost_amount'
            ]}
         ),

        ('Educational Background', {
            'fields': [
                'household_head',
                'profession',
                'education_years',
                'education_certificate',
                'elementary_school',
                'elementary_attendance_years',
                'secondary_school',
                'secondary_attendance_years',
                'higher_education',
                'higher_attendance_years',
                'head_profession',
                'head_education_years',
                'head_education_certificate',
                'head_elementary',
                'head_attendance_years',
                'head_secondary',
                'head_secondary_years',
                'head_higher_education',
                'head_higher_years']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'activities_missed': admin.VERTICAL,
        'care_before_hospital': admin.VERTICAL,
        'care_provider': admin.VERTICAL,
        'cd4_date_estimated': admin.VERTICAL,
        'cryptococcal_lesions': admin.VERTICAL,
        'ecog_score': admin.VERTICAL,
        'elementary_school': admin.VERTICAL,
        'first_arv_regimen': admin.VERTICAL,
        'first_line_choice': admin.VERTICAL,
        'higher_education': admin.VERTICAL,
        'head_elementary': admin.VERTICAL,
        'head_secondary': admin.VERTICAL,
        'household_head': admin.VERTICAL,
        'head_higher_education': admin.VERTICAL,
        'location_care': admin.VERTICAL,
        'lung_exam': admin.VERTICAL,
        'tb_history': admin.VERTICAL,
        'new_hiv_diagnosis': admin.VERTICAL,
        'medication_bought': admin.VERTICAL,
        'other_place_visited': admin.VERTICAL,
        'patient_adherence': admin.VERTICAL,
        'paid_treatment': admin.VERTICAL,
        'second_arv_regimen': admin.VERTICAL,
        'secondary_school': admin.VERTICAL,
        'taking_arv': admin.VERTICAL,
        'taking_rifampicin': admin.VERTICAL,
        'tb_site': admin.VERTICAL,
        'tb_treatment': admin.VERTICAL,
        'transport_form': admin.VERTICAL,
        'vl_date_estimated': admin.VERTICAL,
        'loss_of_earnings': admin.VERTICAL, }
