from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import SubjectRandomizationForm
from ..models import SubjectRandomization
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectRandomization, site=ambition_subject_admin)
class SubjectRandomizationAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectRandomizationForm

    radio_fields = {
        'abnormal_mental_status': admin.VERTICAL,
        'on_arvs': admin.VERTICAL}

    fieldsets = (
        ['First Contact', {
            'fields': (
                'subject_visit',
                'hospital_admission_date',
                'abnormal_mental_status',
                'on_arvs')}],
        audit_fieldset_tuple
    )
