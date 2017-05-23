from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import MicrobiologyForm
from ..models import Microbiology
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Microbiology, site=ambition_subject_admin)
class MicrobiologyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MicrobiologyForm

    radio_fields = {
        'urine_culture_performed': admin.VERTICAL,
        'urine_culture_results': admin.VERTICAL,
        'urine_culture_organism': admin.VERTICAL,
        'blood_culture_performed': admin.VERTICAL,
        'blood_culture_results': admin.VERTICAL,
        'blood_culture_organism': admin.VERTICAL,
        'bacteria_identified': admin.VERTICAL,
        'sputum_results_afb': admin.VERTICAL,
        'sputum_results_culture': admin.VERTICAL,
        'sputum_result_genexpert': admin.VERTICAL,
        'tissue_biopsy_taken': admin.VERTICAL,
        'tissue_biopsy_results': admin.VERTICAL,
        'tissue_biopsy_organism': admin.VERTICAL}

    fieldsets = (
        ['Urine Culture (Only for patients with >50 white cells in urine)', {
            'fields': (
                'subject_visit',
                'urine_culture_performed',
                'urine_culture_results',
                'urine_culture_organism',
                'urine_culture_organism_other')}],
        ['Blood Culture', {
            'fields': (
                'blood_culture_performed',
                'blood_culture_results',
                'date_blood_taken',
                'day_blood_taken',
                'blood_culture_organism',
                'blood_culture_organism_other',
                'bacteria_identified',
                'bacteria_identified_other')}],
        ['Sputum results - Microscopy', {
            'fields': (
                'sputum_results_afb',
                'sputum_results_culture',
                'sputum_results_positive',
                'sputum_result_genexpert')}],
        ['Biopsy', {
            'fields': (
                'tissue_biopsy_taken',
                'tissue_biopsy_results',
                'date_biopsy_taken',
                'day_biopsy_taken',
                'tissue_biopsy_organism',
                'tissue_biopsy_organism_other',
                'histopathology_report')}],
        audit_fieldset_tuple
    )
