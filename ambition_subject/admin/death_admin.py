from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import DeathForm
from ..models import Death
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Death, site=ambition_subject_admin)
class DeathAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = DeathForm

    radio_fields = {
        'death_as_inpatient': admin.VERTICAL,
        'cause_of_death_study_doctor_opinion': admin.VERTICAL,
        'cause_tb_study_doctor_opinion': admin.VERTICAL,
        'cause_of_death_tmg1_opinion': admin.VERTICAL,
        'cause_of_death_agreed': admin.VERTICAL,
        'cause_tb_tmg1_opinion': admin.VERTICAL,
        'cause_of_death_tmg2_opinion': admin.VERTICAL,
        'cause_tb_tmg2_opinion': admin.VERTICAL}

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'study_day',
                'death_as_inpatient')},
         ),
        ('Opinion of Local Study Doctor', {
            'fields': (
                'cause_of_death_study_doctor_opinion',
                'cause_other_study_doctor_opinion',
                'cause_tb_study_doctor_opinion')}),
        ('Opinion of TMG 1', {
            'fields': (
                'cause_of_death_tmg1_opinion',
                'cause_other_tmg1_opinion',
                'cause_tb_tmg1_opinion',
                'cause_of_death_agreed')}),
        ('Opinion of TMG 2', {
            'fields': (
                'cause_of_death_tmg2_opinion',
                'cause_other_tmg2_opinion',
                'cause_tb_tmg2_opinion')}),
        ('Summary', {
            'fields': (
                'death_narrative',)}),
        audit_fieldset_tuple
    )
