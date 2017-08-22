from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import AdverseEventTMGForm
from ..models import AdverseEventTMG
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AdverseEventTMG, site=ambition_subject_admin)
class AdverseEventTMGAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventTMGForm

    fieldsets = (
        ('For completion by TMG Investigator Only', {
            'fields': (
                'subject_visit',
                'ae_received_datetime',
                'clinical_review_datetime',
                'investigator_comments',
                'ae_description',
                'ae_classification',
                'ae_classification_other',
                'officials_notified',
                'investigator_returned')}),
        audit_fieldset_tuple
    )

    filter_horizontal = ('ae_classification',)
