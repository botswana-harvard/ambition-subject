from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import EducationalBackgroundForm
from ..models import EducationalBackground
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(EducationalBackground, site=ambition_subject_admin)
class EducationalBackgroundAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = EducationalBackgroundForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_visit',
                'household_head',
                'head_profession',
                'head_education_years',
                'head_education_certificate',
                'head_elementary',
                'head_attendance_years',
                'head_secondary',
                'head_secondary_years',
                'head_higher_education',
                'head_higher_years']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'head_elementary': admin.VERTICAL,
        'head_secondary': admin.VERTICAL,
        'household_head': admin.VERTICAL,
        'head_higher_education': admin.VERTICAL}
