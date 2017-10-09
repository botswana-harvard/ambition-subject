from django.contrib import admin

from edc_base.fieldsets.fieldset import Fieldset
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import PrnModelForm
from ..models import PrnModel

from .modeladmin_mixins import CrfModelAdminMixin
from ambition_subject.constants import (WEEK4, WEEK6, WEEK8, WEEK10,
                                        DAY1, DAY7, DAY14)

common_fields = ('subject_visit',
                 'adverse_event',
                 'adverse_event_tmg',
                 'adverse_event_followup',
                 'microbiology',
                 'radiology',
                 'protocol_deviation',
                 'death_report',)

week4 = common_fields + ('lumbar_puncture', 'recurrence_symptom',)

follow_up = common_fields + ('lumbar_puncture',
                             'recurrence_symptom',
                             'blood_result')


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
        'adverse_event': admin.VERTICAL,
        'adverse_event_tmg': admin.VERTICAL,
        'adverse_event_followup': admin.VERTICAL,
        'microbiology': admin.VERTICAL,
        'radiology': admin.VERTICAL,
        'lumbar_puncture': admin.VERTICAL,
        'protocol_deviation': admin.VERTICAL,
        'recurrence_symptom': admin.VERTICAL,
        'blood_result': admin.VERTICAL,
        'death_report': admin.VERTICAL, }

    fieldsets = (
        ['PRN', {
            'fields': (
                'subject_visit',
                'adverse_event',
                'adverse_event_tmg',
                'adverse_event_followup',
                'microbiology',
                'lumbar_puncture',
                'radiology',
                'protocol_deviation',
                'death_report',)}],
        audit_fieldset_tuple
    )
