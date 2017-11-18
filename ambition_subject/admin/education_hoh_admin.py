from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import EducationHohForm
from ..models import EducationHoh
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(EducationHoh, site=ambition_subject_admin)
class EducationHohAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = EducationHohForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_visit',
                'profession',
                'education_years',
                'education_certificate',
                'elementary',
                'attendance_years',
                'secondary',
                'secondary_years',
                'higher_education',
                'higher_years']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'elementary': admin.VERTICAL,
        'secondary': admin.VERTICAL,
        'higher_education': admin.VERTICAL}
