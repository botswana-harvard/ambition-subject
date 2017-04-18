from django.contrib import admin

from ..admin_site import ambition_subject_admin
from ..forms import ClinicNoteForm
from ..models import ClinicNote

from .modeladmin_mixins import ModelAdminMixin


@admin.register(ClinicNote, site=ambition_subject_admin)
class ClinicNoteAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ClinicNoteForm
