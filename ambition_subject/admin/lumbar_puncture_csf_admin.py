from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple
from edc_base.fieldsets.fieldset import Fieldset

from ..admin_site import ambition_subject_admin
from ..constants import DAY1
from ..forms import LumbarPunctureCSFForm
from ..models import LumbarPunctureCsf
from .modeladmin_mixins import CrfModelAdminMixin

wbc_count = Fieldset(
    'csf_wbc_cell_count', section='WBC Count')

day1_lp = Fieldset('csf_wbc_cell_count',
                   'differential_lymphocyte_count',
                   'differential_lymphocyte_unit',
                   'differential_neutrophil_count',
                   'differential_neutrophil_unit',
                   'india_ink',
                   'csf_glucose',
                   'csf_glucose_units',
                   'csf_protein',
                   'csf_cr_ag',
                   'csf_cr_ag_lfa', section='Day1')


@admin.register(LumbarPunctureCsf, site=ambition_subject_admin)
class LumbarPunctureCSFAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = LumbarPunctureCSFForm

    conditional_fieldsets = {
        DAY1: day1_lp
    }

    radio_fields = {
        'reason_for_lp': admin.VERTICAL,
        'csf_culture': admin.VERTICAL,
        'india_ink': admin.VERTICAL,
        'csf_cr_ag': admin.VERTICAL,
        'csf_cr_ag_lfa': admin.VERTICAL,
        'differential_lymphocyte_unit': admin.VERTICAL,
        'differential_neutrophil_unit': admin.VERTICAL,
        'csf_glucose_units': admin.VERTICAL}

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
        audit_fieldset_tuple
    )
