from django.contrib import admin

from edc_base.fieldsets.fieldset import Fieldset
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..constants import DAY1, DAY7, DAY14, WEEK4, WEEK6, WEEK8, WEEK10
from ..forms import BloodResultForm
from ..models import BloodResult
from .modeladmin_mixins import CrfModelAdminMixin


blood_count = Fieldset(
    'wbc',
    'platelets',
    'haemoglobin',
    'absolute_neutrophil',
    section='Complete Blood Count (CBC)')

alt = Fieldset(
    'alt',
    section='Liver Function Tests')

urine_chemistry = Fieldset(
    'proteinuria',
    section='Urine Chemistry')

immunology = Fieldset(
    'abs_cd4',
    section='Immunology')


@admin.register(BloodResult, site=ambition_subject_admin)
class BloodResultsAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BloodResultForm
    conditional_fieldsets = {
        DAY1: (alt, urine_chemistry, blood_count, immunology),
        DAY7: (alt, blood_count),
        DAY14: (alt, blood_count),
        WEEK4: (alt, blood_count),
        WEEK6: (blood_count,),
        WEEK8: (blood_count,),
        WEEK10: (blood_count,)}

    fieldsets = (
        [None, {
            'fields': (
                'subject_visit',)}],
        ['Renal Function Tests', {
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

    radio_fields = {
        'proteinuria': admin.VERTICAL,
        'are_results_normal': admin.VERTICAL,
        'abnormal_results_in_ae_range': admin.VERTICAL,
        'creatinine_unit': admin.VERTICAL,
        'magnesium_unit': admin.VERTICAL,
        'urea_unit': admin.VERTICAL}
