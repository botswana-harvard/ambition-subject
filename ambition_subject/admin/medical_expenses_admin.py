from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple
from edc_fieldsets import Fieldset

from ..admin_site import ambition_subject_admin
from ..forms import MedicalExpensesForm
from ..models import MedicalExpenses
from ..constants import DAY1, WEEK10

from .modeladmin_mixins import CrfModelAdminMixin

info_source = Fieldset(
    'info_source',
    section='Information Source')

transport = Fieldset(
    'form_of_transport',
    'transport_fare',
    'travel_time',
    section='Transport'
)

loans_insurance = Fieldset(
    'loans',
    'sold_anything',
    'private_healthcare',
    'healthcare_insurance',
    section='Loans and Insurance'
)

welfare = Fieldset(
    'welfare',
    section='Welfare or social service support'
)


@admin.register(MedicalExpenses, site=ambition_subject_admin)
class MedicalExpensesAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MedicalExpensesForm
    conditional_fieldsets = {
        DAY1: (info_source, transport, loans_insurance, welfare),
        WEEK10: (info_source, loans_insurance)}

    fieldsets = (
        ('Medical Expenses', {
            'fields': [
                'subject_visit',
                'currency',
                'food_spend',
                'utilities_spend',
                'item_spend',
                'personal_he_spend',
                'proxy_he_spend',
                'he_spend_last_4weeks',
                'duration_present_condition',
                'activities_missed',
                'activities_missed_other',
                'time_off_work',
                'carer_time_off',
                'loss_of_earnings',
                'earnings_lost_amount',
                'care_before_hospital',
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'activities_missed': admin.VERTICAL,
        'care_before_hospital': admin.VERTICAL,
        'currency': admin.VERTICAL,
        'loss_of_earnings': admin.VERTICAL,
        'form_of_transport': admin.VERTICAL,
        'loans': admin.VERTICAL,
        'sold_anything': admin.VERTICAL,
        'private_healthcare': admin.VERTICAL,
        'healthcare_insurance': admin.VERTICAL,
        'welfare': admin.VERTICAL}
