from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import AdverseEventFollowUpForm
from ..models import AdverseEventFollowUp
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AdverseEventFollowUp, site=ambition_subject_admin)
class AdverseEventFollowUpAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventFollowUpForm
    fieldsets = (
        ('Clinical Assessment', {
            'fields': (
                'subject_visit',
                'outcome',
                'outcome_date',
                'relevant_history')},
         ),
        audit_fieldset_tuple
    )

    radio_fields = {
        'outcome': admin.VERTICAL}
