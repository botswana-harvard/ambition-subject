from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import ProtocolDeviationViolationForm
from ..models import ProtocolDeviationViolation
from .modeladmin_mixins import ModelAdminMixin


@admin.register(ProtocolDeviationViolation, site=ambition_subject_admin)
class PatientHistoryAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ProtocolDeviationViolationForm

    radio_fields = {
        'protocol_violation_type': admin.VERTICAL,
        'action_required': admin.VERTICAL}

    fieldsets = (
        ('Assessment to confirm violation', {
            'fields': (
                'safety',
                'safety_details',
                'outcomes',
                'outcomes_details')},
         ),
        ('Details of violation', {
            'fields': (
                'date_violation_datetime',
                'protocol_violation_type',
                'description',
                'violation_reason')}
         ),
        ('Actions taken', {
            'fields': (
                'corrective_action_datetime',
                'corrective_action',
                'preventative_action_datetime',
                'preventative_action',
                'action_required',)}),
        audit_fieldset_tuple
    )
