from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import AdverseEventForm
from ..models import AdverseEvent
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AdverseEvent, site=ambition_subject_admin)
class AdverseEventAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventForm

    radio_fields = {
        'ae_cause': admin.VERTICAL}

    fieldsets = (
        ('Initial Report', {
            'fields': (
                'ae_awareness_date',
                'ae_start_date',
                'med_administered_datetime',
                'implicated_med',
                'implicated_med_dose',
                'implicated_med_route',
                'ae_cause',
                'ae_cause_other',
                'ae_treatment',)},
         ),
        audit_fieldset_tuple
    )
