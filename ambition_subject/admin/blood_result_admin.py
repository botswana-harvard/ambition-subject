from django.contrib import admin

from edc_base.fieldsets.fieldset import Fieldset
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..constants import DAY1
from ..forms import BloodResultForm
from ..models import BloodResult
from .modeladmin_mixins import CrfModelAdminMixin

extra_fields = Fieldset(
    'proteinuria',
    'abs_cd4',
    section='Urine tests & CD4 profiles')


@admin.register(BloodResult, site=ambition_subject_admin)
class BloodResultsAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BloodResultForm
    conditional_fieldsets = {
        DAY1: extra_fields, }

    radio_fields = {
        'proteinuria': admin.VERTICAL,
        'are_results_normal': admin.VERTICAL,
        'abnormal_results_in_ae_range': admin.VERTICAL}

    fieldsets = (
        ['Complete Blood Count (CBC)', {
            'fields': (
                'subject_visit',
                'wbc',
                'platelets',
                'haemoglobin',
                'absolute_neutrophil')}],
        ['Chemistry', {
            'fields': (
                'creatinine',
                'sodium',
                'potassium',
                'magnesium',
                'total_bilirubin',
                'alt',
                'crp',
                'urea')}],
        ['Blood test results', {
            'fields': (
                'are_results_normal',
                'abnormal_results_in_ae_range')}],
        audit_fieldset_tuple
    )
