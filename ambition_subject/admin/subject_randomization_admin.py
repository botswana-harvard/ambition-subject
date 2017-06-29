from django.contrib import admin


from ..admin_site import ambition_subject_admin
from ..forms import SubjectRandomizationForm
from ..models import SubjectRandomization
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectRandomization, site=ambition_subject_admin)
class SubjectRandomizationAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectRandomizationForm
