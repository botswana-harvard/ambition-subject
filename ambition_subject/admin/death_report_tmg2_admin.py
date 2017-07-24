from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import DeathReportTMG2Form
from ..models import DeathReportTMG2
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DeathReportTMG2, site=ambition_subject_admin)
class DeathReportTMG2Admin(CrfModelAdminMixin, admin.ModelAdmin):

    form = DeathReportTMG2Form

    radio_fields = {
        'cause_of_death_tmg2_opinion': admin.VERTICAL,
        'cause_tb_tmg2_opinion': admin.VERTICAL}

    fieldsets = (
        ('Opinion of TMG 2', {
            'fields': (
                'subject_visit',
                'cause_of_death_tmg2_opinion',
                'cause_other_tmg2_opinion',
                'cause_tb_tmg2_opinion')}),
        ('Summary', {
            'fields': (
                'death_narrative',)}),
        audit_fieldset_tuple
    )
