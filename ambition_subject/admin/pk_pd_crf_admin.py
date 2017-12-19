from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, StackedInlineMixin
from edc_fieldsets import Fieldset

from ..admin_site import ambition_subject_admin
from ..constants import DAY1, DAY7, DAY14
from ..forms import PkPdCrfForm, PkPdExtraSamplesForm
from ..models import PkPdCrf, PkPdExtraSamples
from .modeladmin_mixins import CrfModelAdminMixin


common_fields = ('blood_sample_one_datetime',
                 'blood_sample_two_datetime',
                 'blood_sample_three_datetime',
                 'blood_sample_four_datetime',
                 'blood_sample_five_datetime')

blood_reason = ('blood_sample_missed',
                'reason_blood_sample_missed')

d7_d14_common = ('pre_dose_lp',
                 'post_dose_lp',
                 'time_csf_sample_taken')

day1_blood = common_fields + blood_reason
day1_samples = (Fieldset('ambisome_dose',
                         'ambisome_started_datetime',
                         'ambisome_ended_datetime',
                         'full_ambisome_dose_given',
                         section='Ambisome'),
                Fieldset(*day1_blood,
                         section='Blood Results'))

day7_blood = (common_fields + ('blood_sample_six_datetime',) + blood_reason)
day7_samples = (Fieldset(*day7_blood,
                         section='Blood Results'),
                Fieldset(d7_d14_common, section='CSF'))

day14_samples = Fieldset(d7_d14_common,
                         section='CSF')


class PkPdExtraSamplesAdmin(StackedInlineMixin, admin.StackedInline):

    model = PkPdExtraSamples
    form = PkPdExtraSamplesForm
    extra = 0

    fieldsets = (
        [None, {
            'fields': ('extra_csf_samples_datetime',
                       'extra_blood_samples_datetime')},
         ], audit_fieldset_tuple)


@admin.register(PkPdCrf, site=ambition_subject_admin)
class PkPdCrfAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = PkPdCrfForm

    inlines = [PkPdExtraSamplesAdmin]

    conditional_fieldsets = {
        DAY1: day1_samples,
        DAY7: day7_samples,
        DAY14: day14_samples
    }

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'albumin',
                'flucytosine_dose',
                'flucytosine_dose_one_datetime',
                'flucytosine_dose_two_datetime',
                'flucytosine_dose_three_datetime',
                'flucytosine_dose_four_datetime',
                'flucytosine_missed',
                'flucytosine_dose_missed',
                'reason_flucytosine_dose_missed',
                'fluconazole_dose_given',
                'fluconazole_dose_datetime',
                'fluconazole_dose_missed',
                'reason_fluconazole_dose_missed')}),
        audit_fieldset_tuple
    )

    radio_fields = {
        'full_ambisome_dose_given': admin.VERTICAL,
        'flucytosine_missed': admin.VERTICAL,
        'flucytosine_dose_missed': admin.VERTICAL,
        'fluconazole_dose_missed': admin.VERTICAL,
        'blood_sample_missed': admin.VERTICAL,
        'pre_dose_lp': admin.VERTICAL,
        'post_dose_lp': admin.VERTICAL}
