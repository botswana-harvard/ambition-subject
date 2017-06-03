from django.contrib import admin

from edc_base.fieldsets.fieldset import Fieldset

from ..admin_site import ambition_subject_admin
from ..constants import WEEK10
from ..forms import FollowUpForm
from ..models import FollowUp
from .modeladmin_mixins import CrfModelAdminMixin

visual_acuity_fieldset = Fieldset(
    'visual_acuity_left_eye',
    'visual_acuity_right_eye',
    section='Visual Acuity')


@admin.register(FollowUp, site=ambition_subject_admin)
class FollowUpAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = FollowUpForm

    conditional_fieldsets = {
        WEEK10: visual_acuity_fieldset, }

    radio_fields = {
        'physical_symptoms': admin.VERTICAL,
        'headache': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'recent_seizure_less_72': admin.VERTICAL,
        'cn_palsy': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'focal_neurology': admin.VERTICAL,
        'fluconazole_dose': admin.VERTICAL,
        'rifampicin_started': admin.VERTICAL}

    fieldsets = (
        ('Clinical Assessment', {
            'fields': (
                'subject_visit',
                'physical_symptoms',
                'headache',
                'glasgow_coma_score',
                'confusion',
                'recent_seizure_less_72',
                'cn_palsy',
                'behaviour_change',
                'focal_neurology',
                'tb_pulmonary_dx',
                'tb_pulmonary_dx_date',
                'extra_pulmonary_tb_dx',
                'extra_tb_pulmonary_dx_date',
                'kaposi_sarcoma_dx',
                'kaposi_sarcoma_dx_date',
                'malaria_dx',
                'malaria_dx_date',
                'bacteraemia_dx',
                'bacteraemia_dx_date',
                'pneumonia_dx',
                'pneumonia_dx_date',
                'diarrhoeal_wasting_dx',
                'diarrhoeal_wasting_dx_date',
                'other_dx')},
         ),
        ('Drug Treatment', {
            'fields': (
                'fluconazole_dose',
                'fluconazole_dose_other',
                'rifampicin_started',
                'rifampicin_start_date',
                'fu_narrative')})
    )
