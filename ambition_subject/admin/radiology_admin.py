from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import RadiologyForm
from ..models import Radiology
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Radiology, site=ambition_subject_admin)
class RadiologyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = RadiologyForm

    radio_fields = {
        'is_cxr_done': admin.VERTICAL,
        'cxr_type': admin.VERTICAL,
        'is_ct_performed': admin.VERTICAL,
        'is_scanned_with_contrast': admin.VERTICAL,
        'brain_imaging_reason': admin.VERTICAL,
        'are_results_abnormal': admin.VERTICAL,
        'abnormal_results_reason': admin.VERTICAL,
        'infiltrate_location': admin.VERTICAL}

    fieldsets = (
        ['CXR', {
            'fields': (
                'is_cxr_done',
                'when_cxr_done',
                'cxr_type',
                'infiltrate_location',
                'cxr_description')}],
        ['CT/MRI Brain', {
            'fields': (
                'is_ct_performed',
                'date_ct_performed',
                'is_scanned_with_contrast',
                'brain_imaging_reason',
                'brain_imaging_reason_other',
                'are_results_abnormal',
                'abnormal_results_reason',
                'abnormal_results_reason_other',
                'if_infarcts_location')}],
        audit_fieldset_tuple
    )
