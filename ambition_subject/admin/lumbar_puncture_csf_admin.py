from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple
from edc_base.fieldsets.fieldset import Fieldset

from ..admin_site import ambition_subject_admin
from ..constants import DAY1
from ..forms import LumbarPunctureCSFForm
from ..models import LumbarPunctureCsf
from .modeladmin_mixins import CrfModelAdminMixin

wbc_fieldset = Fieldset(
    'csf_wbc_cell_count', section='new section')


@admin.register(LumbarPunctureCsf, site=ambition_subject_admin)
class LumbarPunctureCSFAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = LumbarPunctureCSFForm

    conditional_fieldsets = {
        DAY1: wbc_fieldset, }

    radio_fields = {
        'reason_for_lp': admin.VERTICAL,
        'csf_culture': admin.VERTICAL,
        'india_ink': admin.VERTICAL,
        'csf_cr_ag': admin.VERTICAL,
        'csf_cr_ag_lfa': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
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
