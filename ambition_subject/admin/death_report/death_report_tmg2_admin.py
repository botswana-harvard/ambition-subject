from django.contrib import admin

from ...admin_site import ambition_subject_admin
from ...forms import DeathReportTmg2Form
from ...models import DeathReportTmg2
from ..modeladmin_mixins import CrfModelAdminMixin
from .base_death_report_tmg import BaseDeathReportTmg


@admin.register(DeathReportTmg2, site=ambition_subject_admin)
class DeathReportTmg2Admin(BaseDeathReportTmg, CrfModelAdminMixin, admin.ModelAdmin):

    form = DeathReportTmg2Form
