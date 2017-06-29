from django.contrib import admin

from edc_base.fieldsets.fieldset import Fieldset
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..constants import DAY1
from ..forms import BloodResultForm
from ..models import BloodResult
from .modeladmin_mixins import CrfModelAdminMixin

blood_count = Fieldset(
    'wbc',
    'platelets',
    'haemoglobin',
    'absolute_neutrophil',
    'proteinuria',
    'abs_cd4',
    'alt',
    section='Complete Blood Count (CBC)')


@admin.register(BloodResult, site=ambition_subject_admin)
class BloodResultsAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BloodResultForm
    conditional_fieldsets = {
        DAY1: blood_count}

    radio_fields = {
        'proteinuria': admin.VERTICAL,
        'are_results_normal': admin.VERTICAL,
        'abnormal_results_in_ae_range': admin.VERTICAL,
        'creatinine_unit': admin.VERTICAL,
        'magnesium_unit': admin.VERTICAL,
        'urea_unit': admin.VERTICAL}

    fieldsets = (
        [None, {
            'fields': (
                'subject_visit',)}],
        ['Chemistry', {
            'fields': (
                'creatinine',
                'creatinine_unit',
                'sodium',
                'potassium',
                'magnesium',
                'magnesium_unit',
                'urea',
                'urea_unit')}],
        ['Blood test results', {
            'fields': (
                'are_results_normal',
                'abnormal_results_in_ae_range')}],
        audit_fieldset_tuple
    )
