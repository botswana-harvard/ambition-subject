from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import ClinicNoteForm
from ..models import ClinicNote

from .modeladmin_mixins import ModelAdminMixin


@admin.register(ClinicNote, site=ambition_subject_admin)
class ClinicNoteAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ClinicNoteForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'subjective')},
         ),
        ('Examination', {
            'fields': (
                'vital_signs',
                'cvs',
                'resp',
                'neuro')}),
        ('Assessment', {
            'fields': (
                'assessment',)}),
        ('Plan', {
            'fields': (
                'plan',)}),
        audit_fieldset_tuple
    )
