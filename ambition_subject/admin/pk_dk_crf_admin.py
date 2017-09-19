from django.contrib import admin

# from edc_base.fieldsets.fieldset import Fieldset
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import PkDkCrfForm
from ..models import PkDkCrf

from .modeladmin_mixins import CrfModelAdminMixin
from ambition_subject.constants import DAY1, DAY7, DAY14


@admin.register(PkDkCrf, site=ambition_subject_admin)
class PkDkCrfAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = PkDkCrfForm

    radio_fields = {
        'on_art': admin.VERTICAL,
        'other_medication': admin.VERTICAL,
        'full_ambisome_dose_given': admin.VERTICAL,
        'flucytosine_dose_missed': admin.VERTICAL,
        'flucytosine_days_missed': admin.VERTICAL,
        'fluconazole_dose_missed': admin.VERTICAL,
        'any_day_one_sample_missed': admin.VERTICAL,
        'any_day_seven_sample_missed': admin.VERTICAL,
        'pre_dose_lp': admin.VERTICAL,
        'post_dose_lp': admin.VERTICAL,
        'time_csf_sample_taken': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'weight',
                'cd4_cell_count',
                'on_art',
                'other_medication',
                'albumin',
                'creatine_clearance'
                'potassium',
                'magnesium',
                'haemoglobin',
                'ambisome_dose',
                'ambisome_dose_time_started',
                'ambisome_dose_time_ended',
                'full_ambisome_dose_given',
                'flucytosine_dose',
                'flucytosine_dose_one_time',
                'flucytosine_dose_two_time',
                'flucytosine_dose_three_time',
                'flucytosine_dose_four_time',
                'flucytosine_days_missed',
                'flucytosine_dose_missed',
                'reason_flucytosine_dose_missed',
                'fluconazole_dose_given',
                'time_fluconazole_dose_given',
                'fluconazole_dose_missed',
                'reason_fluconazole_dose_missed',
                'time_blood_sample_one_taken_day_one',
                'time_blood_sample_two_taken_day_one',
                'time_blood_sample_three_taken_day_one',
                'time_blood_sample_four_taken_day_one',
                'time_blood_sample_five_taken_day_one',
                'any_day_one_sample_missed',
                'reason_day_one_missed',
                'blood_sample_one_day_seven',
                'blood_sample_two_day_seven',
                'blood_sample_three_day_seven',
                'blood_sample_four_day_seven',
                'blood_sample_five_day_seven',
                'blood_sample_six_day_seven',
                'any_day_seven_sample_missed',
                'reason_missed_blood_sample_day_seven',
                'pre_dose_lp',
                'post_dose_lp',
                'time_csf_sample_taken',
                'extra_csf_samples_time',
                'extra_csf_samples_date',
                'extra_blood_samples_time',
                'extra_blood_samples_date')}),
        audit_fieldset_tuple
    )
