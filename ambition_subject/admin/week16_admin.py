from django.contrib import admin

from ..admin_site import ambition_subject_admin
from ..forms import Week16Form
from ..models import Week16
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Week16, site=ambition_subject_admin)
class Week16Admin(ModelAdminMixin, admin.ModelAdmin):

    form = Week16Form
