from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple, TabularInlineMixin

from ..admin_site import ambition_subject_admin
from ..forms import HealthEconomicsQuestionnaireForm
from ..forms import HealthEconomicsQuestionnaire2Form
from ..models import HealthEconomicsQuestionnaire
from ..models import HealthEconomicsQuestionnaire2
from .modeladmin_mixins import CrfModelAdminMixin


class HealthEconomicsQuestionnaire2Inline(TabularInlineMixin, admin.StackedInline):

    model = HealthEconomicsQuestionnaire2
    form = HealthEconomicsQuestionnaire2Form
    extra = 1

    list_display = ('location_care', 'location_care_other', 'transport_form')

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

    inlines = [HealthEconomicsQuestionnaire2Inline]

    fieldsets = (
        ('Health Economics Questionnaire', {
            'fields': [
                'subject_visit',
            ]}
         ), audit_fieldset_tuple)
