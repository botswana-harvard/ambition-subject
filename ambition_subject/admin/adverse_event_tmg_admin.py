from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import AdverseEventTMGForm
from ..models import AdverseEventTMG
from .modeladmin_mixins import ModelAdminMixin


@admin.register(AdverseEventTMG, site=ambition_subject_admin)
class AdverseEventTMGAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AdverseEventTMGForm

    filter_horizontal = ('ae_classification',)

    fieldsets = (
        ('For completion by TMG Investigator Only', {
            'fields': (
                'ae_form_received_datetime',
                'clinical_review_datetime',
                'investigator_comments',
                'investigator_ae_description',
                'ae_classification',
                'regulatory_officials_notified_datetime')}),
        audit_fieldset_tuple
    )
