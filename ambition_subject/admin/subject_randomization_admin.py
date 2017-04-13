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
        # 'sex': admin.VERTICAL,
        # 'is_of_age': admin.VERTICAL,
        # 'meningitis_diagoses_by_csf_or_crag': admin.VERTICAL,
        # 'consent_to_hiv_test': admin.VERTICAL,
        # 'willing_to_give_informed_consent': admin.VERTICAL,
        # 'pregrancy_or_lactation': admin.VERTICAL,
        # 'previous_adverse_drug_reaction': admin.VERTICAL,
        # 'medication_contraindicated_with_study_drug': admin.VERTICAL,
        # 'two_days_amphotericin_b': admin.VERTICAL,
        # 'two_days_fluconazole': admin.VERTICAL,
        # 'patient_eligible': admin.VERTICAL,
        # 'consent_given': admin.VERTICAL,
        'abnormal_mental_status': admin.VERTICAL,
        'already_on_arvs': admin.VERTICAL,
        'randomization_number': admin.VERTICAL,
        'consent_form_signed': admin.VERTICAL,
        'regimen': admin.VERTICAL}

    fieldsets = (
        ['Inclusion Criteria', {
            'fields': (
                # 'is_of_age',
                # 'meningitis_diagoses_by_csf_or_crag',
                # 'consent_to_hiv_test',
                # 'willing_to_give_informed_consent'
                )}],
        ['Exclusion Criteria', {
            'fields': (
                # 'pregrancy_or_lactation',
                # 'previous_adverse_drug_reaction',
                # 'medication_contraindicated_with_study_drug',
                # 'two_days_amphotericin_b',
                # 'two_days_fluconazole'
                )}],
        ['First Contact', {
            'fields': (
                # 'age',
                # 'sex',
                # 'patient_eligible',
                # 'consent_given',
                'hospital_admission_date',
                'inclusion_date',
                'abnormal_mental_status',
                'already_on_arvs',
                'arv_start_date',
                'randomization_number',
                'consent_form_signed',
                'regimen')}],
        audit_fieldset_tuple
    )
