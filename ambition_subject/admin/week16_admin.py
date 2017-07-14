from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import Week16Form
from ..models import Week16
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Week16, site=ambition_subject_admin)
class Week16Admin(ModelAdminMixin, admin.ModelAdmin):

    form = Week16Form

    radio_fields = {
        'patient_alive': admin.VERTICAL,
        'activities_help': admin.VERTICAL,
        'illness_problems': admin.VERTICAL,
        'ranking_score': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'patient_alive',
                'death_datetime',
                'activities_help',
                'illness_problems',
                'ranking_score',
            )},
         ),
        audit_fieldset_tuple)
