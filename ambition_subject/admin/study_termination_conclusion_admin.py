from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

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
        'willing_to_complete_10W_FU': admin.VERTICAL,
        'willing_to_complete_centre': admin.VERTICAL,
        'late_protocol_exclusion': admin.VERTICAL,
        'rifampicin_started': admin.VERTICAL,
        'first_line_regimen_patients': admin.VERTICAL,
        'second_line_regimen_patients': admin.VERTICAL,
        'first_line_env': admin.VERTICAL}

    fieldsets = (
        [None, {
            'fields': (
                'subject_visit',
                'date_patient_terminated',
                'date_last_study_fu',
                'discharged_after_initial_admission',
                'date_initial_discharge',
                'readmission_after_initial_discharge',
                'date_readmission',
                'date_discharged',
                'termination_reason',
                'death_date',
                'consent_withdrawal_reason',
                'willing_to_complete_10W_FU',
                'willing_to_complete_centre',
                'date_willing_to_complete',
                'late_protocol_exclusion',
                'rifampicin_started',
                'included_in_error',
                'first_line_regimen_patients',
                'first_line_regimen_patients_other',
                'second_line_regimen_patients',
                'second_line_regimen_patients_other',
                'date_arvs_started_or_switched',
                'first_line_env',
                'arvs_delay_reason')}],
        audit_fieldset_tuple
    )
