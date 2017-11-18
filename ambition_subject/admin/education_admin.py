from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import EducationForm
from ..models import Education
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(Education, site=ambition_subject_admin)
class EducationAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = EducationForm

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
                'higher_years',
                'household_head']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'household_head': admin.VERTICAL,
        'elementary': admin.VERTICAL,
        'secondary': admin.VERTICAL,
        'household_head': admin.VERTICAL,
        'higher_education': admin.VERTICAL}
