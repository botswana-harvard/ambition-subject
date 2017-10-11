from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple, TabularInlineMixin

from ..admin_site import ambition_subject_admin
from ..forms import HealthEconomicsQuestionnaireForm, MedicalExpensesForm
from ..models import HealthEconomicsQuestionnaire, MedicalExpenses
from .modeladmin_mixins import CrfModelAdminMixin


class MedicalExpensesInline(TabularInlineMixin, admin.StackedInline):

    model = MedicalExpenses
    form = MedicalExpensesForm
    extra = 1

    list_display = ('care_before_hospital', 'location_care',
                    'location_care_other', 'transport_form')

    fieldsets = (
        ['Medical Expenses Continued..', {
            'fields': (
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
                'other_place_visited')},
         ],)

    radio_fields = {
        'care_provider': admin.VERTICAL,
        'medication_bought': admin.VERTICAL,
        'location_care': admin.VERTICAL,
        'other_place_visited': admin.VERTICAL,
        'paid_treatment': admin.VERTICAL,
        'transport_form': admin.VERTICAL}


@admin.register(HealthEconomicsQuestionnaire, site=ambition_subject_admin)
class HealthEconomicsQuestionnaireAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = HealthEconomicsQuestionnaireForm

    inlines = [MedicalExpensesInline]

    fieldsets = (
        ('Medical Expenses', {
            'fields': [
                'subject_visit',
                'currency',
                'personal_he_spend',
                'proxy_he_spend',
                'he_spend_last_4weeks',
                'care_before_hospital',
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
        'currency': admin.VERTICAL,
        'elementary_school': admin.VERTICAL,
        'higher_education': admin.VERTICAL,
        'head_elementary': admin.VERTICAL,
        'head_secondary': admin.VERTICAL,
        'household_head': admin.VERTICAL,
        'head_higher_education': admin.VERTICAL,
        'location_care': admin.VERTICAL,
        'medication_bought': admin.VERTICAL,
        'other_place_visited': admin.VERTICAL,
        'secondary_school': admin.VERTICAL,
        'transport_form': admin.VERTICAL,
        'loss_of_earnings': admin.VERTICAL}
