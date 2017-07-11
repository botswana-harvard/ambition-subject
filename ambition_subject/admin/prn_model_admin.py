from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import PrnModelForm
from ..models import PrnModel

from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(PrnModel, site=ambition_subject_admin)
class PrnModelAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = PrnModelForm

    radio_fields = {
        'adverse_event': admin.VERTICAL,
        'adverse_event_tmg': admin.VERTICAL,
        'adverse_event_followup': admin.VERTICAL,
        'microbiology': admin.VERTICAL,
        'radiology': admin.VERTICAL,
        'lumbar_puncture': admin.VERTICAL,
        'protocol_deviation': admin.VERTICAL,
        'death_report': admin.VERTICAL}

    fieldsets = (
        ['PRN', {
            'fields': (
                'subject_visit',
                'adverse_event',
                'adverse_event_tmg',
                'adverse_event_followup',
                'microbiology',
                'radiology',
                'protocol_deviation',
                'lumbar_puncture',
                'death_report')}],
        audit_fieldset_tuple
    )
