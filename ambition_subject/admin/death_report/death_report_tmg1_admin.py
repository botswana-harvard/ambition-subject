from django.contrib import admin

from ...admin_site import ambition_subject_admin
from ...forms import DeathReportTmg1Form
from ...models import DeathReportTmg1
from ..modeladmin_mixins import CrfModelAdminMixin
from .base_death_report_tmg import BaseDeathReportTmg


@admin.register(DeathReportTmg1, site=ambition_subject_admin)
class DeathReportTmg1Admin(BaseDeathReportTmg, CrfModelAdminMixin, admin.ModelAdmin):

    form = DeathReportTmg1Form
