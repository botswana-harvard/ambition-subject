from ambition_subject.admin_site import ambition_subject_admin
from ambition_subject.forms import SubjectOffStudyForm
from ambition_subject.models import SubjectOffstudy
# from edc_base.modeladmin_mixins import audit_fieldset_tuple

from django.contrib import admin

from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectOffstudy, site=ambition_subject_admin)
class SubjectOffStudyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectOffStudyForm
