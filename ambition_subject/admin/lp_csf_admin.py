from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import LpCsfForm
from ..models import LpCsf
from .modeladmin_mixins import ModelAdminMixin


@admin.register(LpCsf, site=ambition_subject_admin)
class LpCsfAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = LpCsfForm

    radio_fields = {
        'reason_for_lp': admin.VERTICAL,
        'csf_culture': admin.VERTICAL,
        'india_ink': admin.VERTICAL,
        'csf_cr_ag': admin.VERTICAL,
        'csf_cr_ag_lfa': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'reason_for_lp',
                'opening_pressure',
                'closing_pressure',
                'csf_amount_removed',
                'quantitative_culture',
                'csf_culture',
                'other_csf_culture')},
         ),
        ('Complete the following for D1 LP only', {
            'fields': (
                'csf_wbc_cell_count',
                'differential_lymphocyte_count',
                'differential_neutrophil_count',
                'india_ink',
                'csf_glucose',
                'csf_protein',
                'csf_cr_ag',
                'csf_cr_ag_titres',
                'csf_cr_ag_lfa')}),
        audit_fieldset_tuple
    )
