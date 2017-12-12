from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from edc_fieldsets import Fieldset

from ..admin_site import ambition_subject_admin
from ..constants import WEEK4, WEEK6, WEEK8, WEEK10, DAY1, DAY7, DAY14
from ..forms import PrnModelForm
from ..models import PrnModel

from .modeladmin_mixins import CrfModelAdminMixin


# requisitions = Fieldset(
#     'viral_load',
#     'cd4',
#     section='Requisitions')

common_fields = ('subject_visit',
                 'microbiology',
                 'radiology',
                 'cd4',
                 'viral_load',
                 'fbc',
                 'chemistry')

week4 = common_fields + ('lumbar_puncture', )

follow_up = common_fields + ('lumbar_puncture',
                             'blood_result',)


@admin.register(PrnModel, site=ambition_subject_admin)
class PrnModelAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = PrnModelForm
    conditional_fieldsets = {
        DAY1: Fieldset(*common_fields, section='PRN'),
        DAY7: Fieldset(*common_fields, section='PRN'),
        DAY14: Fieldset(*common_fields, section='PRN'),
        WEEK4: Fieldset(*week4, section='PRN'),
        WEEK6: Fieldset(*follow_up, section='PRN'),
        WEEK8: Fieldset(*follow_up, section='PRN'),
        WEEK10: Fieldset(*follow_up, section='PRN'), }

    radio_fields = {
        'microbiology': admin.VERTICAL,
        'radiology': admin.VERTICAL,
        'lumbar_puncture': admin.VERTICAL,
        'blood_result': admin.VERTICAL,
        'viral_load': admin.VERTICAL,
        'cd4': admin.VERTICAL, }

    fieldsets = (
        ['PRN', {
            'fields': (
                'subject_visit',
                'microbiology',
                'lumbar_puncture',
                'radiology',)}],
        audit_fieldset_tuple
    )
