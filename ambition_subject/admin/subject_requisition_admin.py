from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from edc_lab.admin import (
    RequisitionAdminMixin,
    requisition_fieldset,
    requisition_status_fieldset,
    requisition_identifier_fieldset,
    requisition_identifier_fields)

from ..admin_site import ambition_subject_admin
from ..models import SubjectRequisition
from ..forms import SubjectRequisitionForm
from .modeladmin_mixins import CrfModelAdminMixin
from pprint import pprint
from urllib.parse import parse_qs, urlsplit


@admin.register(SubjectRequisition, site=ambition_subject_admin)
class SubjectRequisitionAdmin(CrfModelAdminMixin,
                              RequisitionAdminMixin,
                              admin.ModelAdmin):

    # show_save_next = False

    form = SubjectRequisitionForm

    ordering = ('requisition_identifier', )

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'requisition_datetime',
                'panel_name',
            )}),
        requisition_fieldset,
        requisition_status_fieldset,
        requisition_identifier_fieldset,
        audit_fieldset_tuple)

    radio_fields = {
        'is_drawn': admin.VERTICAL,
        'reason_not_drawn': admin.VERTICAL,
        'item_type': admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + requisition_identifier_fields)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        path = urlsplit(request.META.get('HTTP_REFERER')).path
        query = urlsplit(request.META.get('HTTP_REFERER')).query
        if 'bloodresult' in path:
            attrs = parse_qs(query)
            try:
                subject_visit = attrs.get('subject_visit')[0]
            except IndexError:
                pass
            else:
                queryset = queryset.filter(subject_visit__id=subject_visit)
        return queryset, use_distinct
