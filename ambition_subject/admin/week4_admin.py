from django.contrib import admin

from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import Week4Form
from ..models import Week4

from .modeladmin_mixins import ModelAdminMixin


@admin.register(Week4, site=ambition_subject_admin)
class Week4Admin(ModelAdminMixin, admin.ModelAdmin):

    form = Week4Form

    fieldsets = (
        ['Clinical Assessment', {
            'fields': (
                'headache',
                'temperature',
                'glasgow_cs',
                'recent_seizure_less_72',
                'behaviour_change',
                'confusion',
                'cn_palsy',
                'focal_neurology',
                'weight',
                'significant_new_diagnosis')}
         ],
        audit_fieldset_tuple
    )

    radio_fields = {
        'physical_symptoms': admin.VERTICAL,
        'headache': admin.VERTICAL,
        'recent_seizure_less_72': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'cn_palsy': admin.VERTICAL,
        'focal_neurology': admin.VERTICAL,
    }
