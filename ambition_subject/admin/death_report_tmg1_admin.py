from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import DeathReportTMG1Form
from ..models import DeathReportTMG1
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(DeathReportTMG1, site=ambition_subject_admin)
class DeathReportTMG1Admin(CrfModelAdminMixin, admin.ModelAdmin):

    form = DeathReportTMG1Form

    radio_fields = {
        'cause_of_death_tmg1_opinion': admin.VERTICAL,
        'cause_of_death_agreed': admin.VERTICAL,
        'cause_tb_tmg1_opinion': admin.VERTICAL}

    fieldsets = (
        ('Opinion of TMG 1', {
            'fields': (
                'subject_visit',
                'cause_of_death_tmg1_opinion',
                'cause_other_tmg1_opinion',
                'cause_tb_tmg1_opinion',
                'cause_of_death_agreed')}),
        ('Summary', {
            'fields': (
                'death_narrative',)}),
        audit_fieldset_tuple
    )
