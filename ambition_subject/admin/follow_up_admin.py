from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin
from edc_fieldsets import Fieldset

from ..admin_site import ambition_subject_admin
from ..constants import WEEK10
from ..forms import FollowUpForm, FollowUpDiagnosesForm
from ..models import FollowUp, FollowUpDiagnoses
from .modeladmin_mixins import CrfModelAdminMixin

visual_acuity_fieldset = Fieldset(
    'visual_acuity_left_eye',
    'visual_acuity_right_eye',
    'patient_help',
    'patient_problems',
    'ranking_score',
    section='Disability Assessment')


class FollowUpDiagnosesInline(TabularInlineMixin, admin.TabularInline):

    model = FollowUpDiagnoses
    form = FollowUpDiagnosesForm
    extra = 1

    fieldsets = (
        ['Admission history', {
            'fields': (
                'possible_diagnoses',
                'dx_date',
                'dx_other')},
         ],)


@admin.register(FollowUp, site=ambition_subject_admin)
class FollowUpAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = FollowUpForm

    inlines = [FollowUpDiagnosesInline]

    conditional_fieldsets = {
        WEEK10: visual_acuity_fieldset, }

    fieldsets = (
        ('Clinical Assessment', {
            'fields': (
                'subject_visit',
                'physical_symptoms',
                'headache',
                'glasgow_coma_score',
                'confusion',
                'recent_seizure_less_72',
                'cn_palsy',
                'behaviour_change',
                'focal_neurology')},
         ),
        ('Drug Treatment', {
            'fields': (
                'fluconazole_dose',
                'fluconazole_dose_other',
                'rifampicin_started',
                'rifampicin_start_date')}),

        #         ('Medical Expenses', {
        #             'fields': [
        #                 # 'personal_he_spend',
        #                 # 'proxy_he_spend',
        #                 'he_spend_last_4weeks',
        #                 'location_care_other',
        #                 'transport_cost',
        #                 'transport_duration',
        #                 'care_provider_other',
        #                 'paid_treatment',
        #                 'paid_treatment_amount',
        #                 'medication_payment',
        #                 'duration_present_condition',
        #                 'activities_missed_other',
        #                 'time_off_work',
        #                 'carer_time_off',
        #                 'earnings_lost_amount',
        #                 'other_significant_dx',
        #             ]}
        #          ),
        audit_fieldset_tuple
    )

    radio_fields = {
        'physical_symptoms': admin.VERTICAL,
        'headache': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'recent_seizure_less_72': admin.VERTICAL,
        'cn_palsy': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'focal_neurology': admin.VERTICAL,
        'fluconazole_dose': admin.VERTICAL,
        'rifampicin_started': admin.VERTICAL,
        'other_significant_dx': admin.VERTICAL,
        'patient_help': admin.VERTICAL,
        'patient_problems': admin.VERTICAL,
        'ranking_score': admin.VERTICAL, }
