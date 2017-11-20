from django.contrib import admin

from ..admin_site import ambition_subject_admin
from ..forms import SubjectOffStudyForm
from ..models import SubjectOffstudy
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectOffstudy, site=ambition_subject_admin)
class SubjectOffStudyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectOffStudyForm
