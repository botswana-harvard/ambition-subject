from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import RecurrenceSymptomForm
from ..models import RecurrenceSymptom
from .modeladmin_mixins import ModelAdminMixin


@admin.register(RecurrenceSymptom, site=ambition_subject_admin)
class RecurrenceSymptomAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = RecurrenceSymptomForm

    filter_horizontal = ('antibiotic_treatment' ),

    radio_fields = {
        'patient_readmitted': admin.VERTICAL,
        'recent_seizure': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'lp_completed': admin.VERTICAL,
        'amb_administered': admin.VERTICAL,
        'tb_treatment': admin.VERTICAL,
        'steroids_administered': admin.VERTICAL,
        'steroids_choices': admin.VERTICAL,
        'on_arvs': admin.VERTICAL,
        'arvs_stopped': admin.VERTICAL,
        'dr_opinion': admin.VERTICAL,
    }

    fieldsets = (
        (None, {
            'fields': [
                'subject_visit',
                'patient_readmitted']}
         ),
        ('Glasgow Coma Score', {
            'fields': [
                'glasgow_coma_score']}
         ),
        ('Mental Status', {
            'fields': [
                'recent_seizure',
                'behaviour_change',
                'confusion']}
         ),
        ('Neurological', {
            'fields': [
                'neurological',
                'antibiotic_treatment',
                'focal_neurologic_deficit',
                'cn_palsy']}
         ),
        ('Management', {
            'fields': [
                'lp_completed',
                'amb_administered',
                'amb_duration',
                'tb_treatment',
                'steroids_administered',
                'steroids_duration',
                'steroids_choices',
                'steroids_choices_other',
                'CD4_count',
                'on_arvs',
                'arv_date',
                'arvs_stopped']}
         ),
        ('Forms completed', {
            'fields': [
                'narrative_summary',
                'dr_opinion',
                'dr_opinion_other']}
         ), audit_fieldset_tuple)
