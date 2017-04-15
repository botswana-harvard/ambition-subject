from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import BloodResultsForm
from ..models import BloodResults
from .modeladmin_mixins import ModelAdminMixin


@admin.register(BloodResults, site=ambition_subject_admin)
class BloodResultsAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = BloodResultsForm

    radio_fields = {
        'proteinuria': admin.VERTICAL,
        'urine_cr_ag': admin.VERTICAL,
        'are_results_normal': admin.VERTICAL,
        'abnormal_results_in_ae_range': admin.VERTICAL}

    fieldsets = (
        ['Complete Blood Count (CBC)', {
            'fields': (
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
        ['CD4 profiles', {
            'fields': (
                'abs_cd4',)}],
        ['Urine tests', {
            'fields': (
                'proteinuria',
                'urine_cr_ag')}],
        ['Blood test results', {
            'fields': (
                'are_results_normal',
                'abnormal_results_in_ae_range')}],
        audit_fieldset_tuple
    )
