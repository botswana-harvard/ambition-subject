from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from .modeladmin_mixins import ModelAdminMixin

from ..admin_site import ambition_subject_admin
from ..forms import PatientHistoryForm
from ..models import PatientHistory


@admin.register(PatientHistory, site=ambition_subject_admin)
class AdverseEventAdmin(admin.ModelAdmin, ModelAdminMixin):

    form = PatientHistoryForm
