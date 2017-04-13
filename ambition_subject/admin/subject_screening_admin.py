from django.contrib import admin

from ..admin_site import ambition_subject_admin
from ..models import SubjectScreening

from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectScreening, site=ambition_subject_admin)
class SubjectScreeningAdmin(ModelAdminMixin, admin.ModelAdmin):

    radio_fields = {
        'sex': admin.VERTICAL,
        'is_of_age': admin.VERTICAL,
        'meningitis_diagoses_by_csf_or_crag': admin.VERTICAL,
        'consent_to_hiv_test': admin.VERTICAL,
        'willing_to_give_informed_consent': admin.VERTICAL,
        'pregrancy_or_lactation': admin.VERTICAL,
        'previous_adverse_drug_reaction': admin.VERTICAL,
        'medication_contraindicated_with_study_drug': admin.VERTICAL,
        'two_days_amphotericin_b': admin.VERTICAL,
        'two_days_fluconazole': admin.VERTICAL,
        'patient_eligible': admin.VERTICAL, }
