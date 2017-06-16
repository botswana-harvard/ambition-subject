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
        'microbiology': admin.VERTICAL,
        'radiology': admin.VERTICAL,
        'recurrence_symptom': admin.VERTICAL,
        'protocol_deviation': admin.VERTICAL}

    fieldsets = (
        ['PRN', {
            'fields': (
                'subject_visit',
                'adverse_event',
                'microbiology',
                'radiology',
                'recurrence_symptom',
                'protocol_deviation')}],
        audit_fieldset_tuple
    )
