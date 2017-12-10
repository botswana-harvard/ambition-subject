from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ...admin_site import ambition_subject_admin
from ...forms import BloodResultForm
from ...models import BloodResult
from ..modeladmin_mixins import CrfModelAdminMixin
from .fieldsets import fs, conditional_fieldsets


@admin.register(BloodResult, site=ambition_subject_admin)
class BloodResultsAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BloodResultForm

    conditional_fieldsets = conditional_fieldsets
    fieldsets_move_to_end = ['Conclusion',
                             'Summary', 'Action', audit_fieldset_tuple[0]]

    fieldsets = (
        [None, {'fields': ('subject_visit',)}],
        fs.get('creatinine').fieldset,
        fs.get('sodium').fieldset,
        fs.get('potassium').fieldset,
        fs.get('magnesium').fieldset,
        fs.get('urea').fieldset,
        ['Conclusion', {
            'fields': (
                'results_abnormal',
                'results_reportable')}],
        ['Summary', {'classes': ('collapse', ), 'fields': ('summary', )}],
        ['Action', {'classes': ('collapse', ), 'fields': (
            'tracking_identifier', 'action_identifier')}],
        audit_fieldset_tuple
    )

    radio_fields = {
        'results_abnormal': admin.VERTICAL,
        'results_reportable': admin.VERTICAL,
        'bios_crag': admin.VERTICAL,
        'crag_control_result': admin.VERTICAL,
        'crag_t1_result': admin.VERTICAL,
        'crag_t2_result': admin.VERTICAL,
    }

    readonly_fields = ('summary', 'tracking_identifier', 'action_identifier')

    list_display = ('subject_visit', 'abnormal',
                    'reportable', 'tracking_identifier', 'action_identifier')

    list_filter = ('results_abnormal', 'results_reportable',)

    search_fields = ('tracking_identifier', 'action_identifier', )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'appointment' and request.GET.get('appointment'):
            kwargs["queryset"] = db_field.related_model.objects.filter(
                pk=request.GET.get('appointment', 0))
        return super().formfield_for_foreignkey(
            db_field, request, **kwargs)
