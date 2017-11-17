from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import MedicalExpensesForm
from ..models import MedicalExpenses
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(MedicalExpenses, site=ambition_subject_admin)
class MedicalExpensesAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = MedicalExpensesForm

    fieldsets = (
        ('Medical Expenses', {
            'fields': [
                'subject_visit',
                'currency',
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
                'care_before_hospital'
            ]}
         ), audit_fieldset_tuple)

    radio_fields = {
        'activities_missed': admin.VERTICAL,
        'care_before_hospital': admin.VERTICAL,
        'currency': admin.VERTICAL,
        'loss_of_earnings': admin.VERTICAL}
