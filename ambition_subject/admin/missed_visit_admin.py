from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import MissedVisitForm
from ..models import MissedVisit
from .modeladmin_mixins import ModelAdminMixin


@admin.register(MissedVisit, site=ambition_subject_admin)
class MissedVisitAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = MissedVisitForm

    filter_horizontal = ('reason_visit_missed',)

    fieldsets = (
        [None, {
            'fields': (
                'missed_study_visit_date',
                'visit_missed',
                'reason_visit_missed',
                'reason_visit_missed_other',
                'notes_or_action_taken')}],
        audit_fieldset_tuple
    )
