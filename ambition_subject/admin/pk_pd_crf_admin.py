from django.contrib import admin

from edc_base.fieldsets.fieldset import Fieldset
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..constants import DAY1, DAY7, DAY14
from ..forms import PkPdCrfForm
from ..models import PkPdCrf

from .modeladmin_mixins import CrfModelAdminMixin


common_fields = ('flucytosine_dose',
                 'flucytosine_dose_one_time',
                 'flucytosine_dose_two_time',
                 'flucytosine_dose_three_time',
                 'flucytosine_dose_four_time',
                 'flucytosine_doses_missed',
                 'flucytosine_dose_missed',
                 'reason_flucytosine_dose_missed',
                 'fluconazole_dose_given',
                 'time_fluconazole_dose_given',
                 'fluconazole_dose_missed',
                 'reason_fluconazole_dose_missed')

first_sample = ('ambisome_dose',
                'ambisome_dose_time_started',
                'ambisome_dose_time_ended',
                'full_ambisome_dose_given',
                'blood_sample_one_day_one',
                'blood_sample_two_day_one',
                'blood_sample_three_day_one',
                'blood_sample_four_day_one')

second_sample = ('blood_sample_one_day_seven',
                 'blood_sample_two_day_seven',
                 'blood_sample_three_day_seven',
                 'blood_sample_four_day_seven',
                 'blood_sample_five_day_seven',
                 'blood_sample_six_day_seven',
                 'any_day_seven_sample_missed',
                 'reason_day_seven_missed',
                 'pre_dose_lp',
                 'post_dose_lp',
                 'time_csf_sample_taken')

day1 = common_fields + first_sample + ('albumin',
                                       'creatine_clearance',
                                       'magnesium',
                                       'haemoglobin')

day7 = common_fields + second_sample + ('albumin',
                                        'creatine',
                                        'magnesium',
                                        'haemoglobin')

day14 = common_fields + ('albumin',
                         'creatine',
                         'magnesium',
                         'haemoglobin',
                         'pre_dose_lp',
                         'post_dose_lp',
                         'time_csf_sample_taken')


@admin.register(PkPdCrf, site=ambition_subject_admin)
class PkPdCrfAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = PkPdCrfForm
    conditional_fieldsets = {
        DAY1: Fieldset(*day1, section='Pk and Dk Crf'),
        DAY7: Fieldset(*day7, section='Pk and Dk Crf'),
    }
    radio_fields = {
        'on_art': admin.VERTICAL,
        'other_medication': admin.VERTICAL,
        'full_ambisome_dose_given': admin.VERTICAL,
        'flucytosine_dose_missed': admin.VERTICAL,
        'flucytosine_doses_missed': admin.VERTICAL,
        'fluconazole_dose_missed': admin.VERTICAL,
        'any_day_one_sample_missed': admin.VERTICAL,
        'any_day_seven_sample_missed': admin.VERTICAL,
        'pre_dose_lp': admin.VERTICAL,
        'post_dose_lp': admin.VERTICAL,
        'time_csf_sample_taken': admin.VERTICAL}

    fieldsets = (
        ('Pk and DK Crf', {
            'fields': (
                'weight',
                'cd4_cell_count',
                'on_art',
                'other_medication',
                'albumin',
                'creatine_clearance',
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
                'flucytosine_doses_missed',
                'flucytosine_dose_missed',
                'reason_flucytosine_dose_missed',
                'fluconazole_dose_given',
                'time_fluconazole_dose_given',
                'fluconazole_dose_missed',
                'reason_fluconazole_dose_missed',
                'blood_sample_one_day_one',
                'blood_sample_two_day_one',
                'blood_sample_three_day_one',
                'blood_sample_four_day_one',
                'blood_sample_five_day_one',
                'any_day_one_sample_missed',
                'reason_day_one_missed',
                'blood_sample_one_day_seven',
                'blood_sample_two_day_seven',
                'blood_sample_three_day_seven',
                'blood_sample_four_day_seven',
                'blood_sample_five_day_seven',
                'blood_sample_six_day_seven',
                'any_day_seven_sample_missed',
                'reason_day_seven_missed',
                'pre_dose_lp',
                'post_dose_lp',
                'time_csf_sample_taken',
                'extra_csf_samples_time',
                'extra_csf_samples_date',
                'extra_blood_samples_time',
                'extra_blood_samples_date')}),
        audit_fieldset_tuple
    )
