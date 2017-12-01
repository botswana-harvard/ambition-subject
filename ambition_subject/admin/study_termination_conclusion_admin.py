from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import StudyTerminationConclusionForm
from ..models import StudyTerminationConclusion
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(StudyTerminationConclusion, site=ambition_subject_admin)
class StudyTerminationConclusionAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = StudyTerminationConclusionForm

    radio_fields = {
        'discharged_after_initial_admission': admin.VERTICAL,
        'readmission_after_initial_discharge': admin.VERTICAL,
        'termination_reason': admin.VERTICAL,
        'willing_to_complete_10w': admin.VERTICAL,
        'willing_to_complete_centre': admin.VERTICAL,
        'protocol_exclusion_criterion': admin.VERTICAL,
        'rifampicin_started': admin.VERTICAL,
        'first_line_regimen': admin.VERTICAL,
        'second_line_regimen': admin.VERTICAL,
        'first_line_env': admin.VERTICAL}

    fieldsets = (
        [None, {
            'fields': (
                'subject_visit',
                'patient_terminated_date',
                'last_study_fu_date',
                'discharged_after_initial_admission',
                'initial_discharge_date',
                'readmission_after_initial_discharge',
                'readmission_date',
                'discharged_date',
                'termination_reason',
                'death_date',
                'consent_withdrawal_reason',
                'willing_to_complete_10w',
                'willing_to_complete_centre',
                'willing_to_complete_date',
                'protocol_exclusion_criterion',
                'included_in_error',
                'included_in_error_date',
                'rifampicin_started',
                'first_line_regimen',
                'first_line_regimen_other',
                'second_line_regimen',
                'second_line_regimen_other',
                'arvs_switch_date',
                'first_line_env',
                'arvs_delay_reason')}],
        audit_fieldset_tuple
    )
