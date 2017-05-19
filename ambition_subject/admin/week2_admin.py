from django.contrib import admin

from edc_base.modeladmin_mixins import TabularInlineMixin
from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import Week2Form, AmphotericinMissedDosesForm, FluconazoleMissedDosesForm
from .modeladmin_mixins import ModelAdminMixin
from ..models import Week2, FluconazoleMissedDoses, AmphotericinMissedDoses


class AmphotericinMissedDosesInline(TabularInlineMixin, admin.TabularInline):

    model = AmphotericinMissedDoses
    form = AmphotericinMissedDosesForm
    extra = 1


class FluconazoleMissedDosesInline(TabularInlineMixin, admin.TabularInline):

    model = FluconazoleMissedDoses
    form = FluconazoleMissedDosesForm
    extra = 1


@admin.register(Week2, site=ambition_subject_admin)
class Week2Admin(ModelAdminMixin, admin.ModelAdmin):

    form = Week2Form

    inlines = [FluconazoleMissedDosesInline, AmphotericinMissedDosesInline]

    fieldsets = (
        ['Admission history', {
            'fields': (
                'subject_visit',
                'discharged',
                'discharge_date',
                'died',
                'death_date')},
         ],
        ['Induction phase Study medication', {
            'fields': (
                'flucon_start_datetime',
                'flucon_stop_datetime',
                'antibiotic',
                'blood_received',
                'units')}
         ],
        ['Clinical Assessment', {
            'fields': (
                'headache',
                'temperature',
                'glasgow_cs',
                'seizures_during_admission',
                'recent_seizure',
                'behaviour_change',
                'confusion',
                'cn_palsy',
                'focal_neurology',
                'weight',
                'medicines',
                'significant_diagnosis')}
         ],
        ['Missed Doses', {
            'fields': (
                'flucon_missed_doses',
                'amphotericin_missed_doses')}
         ],
        audit_fieldset_tuple
    )

    radio_fields = {
        'discharged': admin.VERTICAL,
        'died': admin.VERTICAL,
        'flucon_missed_doses': admin.VERTICAL,
        'amphotericin_missed_doses': admin.VERTICAL,
        'blood_received': admin.VERTICAL,
        'blood_received': admin.VERTICAL,
        'headache': admin.VERTICAL,
        'seizures_during_admission': admin.VERTICAL,
        'recent_seizure': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'cn_palsy': admin.VERTICAL,
        'focal_neurology': admin.VERTICAL,
        'medicines': admin.VERTICAL,
        'significant_diagnosis': admin.VERTICAL,
    }
    filter_horizontal = ('antibiotic', )
