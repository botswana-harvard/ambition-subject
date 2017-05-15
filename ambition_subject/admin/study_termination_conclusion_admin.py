from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import StudyTerminationConclusionForm
from ..models import StudyTerminationConclusion
from .modeladmin_mixins import ModelAdminMixin


@admin.register(StudyTerminationConclusion, site=ambition_subject_admin)
class StudyTerminationConclusionAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = StudyTerminationConclusionForm

    radio_fields = {
        'discharged_after_initial_admission': admin.VERTICAL,
        'readmission_following_initial_discharge': admin.VERTICAL,
        'study_termination_reason': admin.VERTICAL,
        'rifampicin_started_since_week4': admin.VERTICAL,
        'arv_regimen': admin.VERTICAL,
        'is_naive': admin.VERTICAL,
        'efv_or_nvp': admin.VERTICAL}

    fieldsets = (
        [None, {
            'fields': (
                'subject_visit',
                'date_patient_terminated_study',
                'termination_study_day',
                'last_research_termination_date',
                'last_research_termination_study_day',
                'discharged_after_initial_admission',
                'initial_discharge_date',
                'initial_discharge_study_date',
                'readmission_following_initial_discharge',
                'date_admitted',
                'date_discharged',
                'study_termination_reason',
                'withdrawal_of_consent_reason',
                'rifampicin_started_since_week4',
                'rifampicin_started_study_day',
                'arv_regimen',
                'is_naive',
                'date_started_arvs',
                'date_switched_arvs',
                'efv_or_nvp')}],
        audit_fieldset_tuple
    )
