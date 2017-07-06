from django.contrib import admin

from edc_base.modeladmin_mixins import TabularInlineMixin
from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..admin_site import ambition_subject_admin
from ..forms import Week2Form, AmphotericinMissedDosesForm, FluconazoleMissedDosesForm, SignificantDiagnosesForm
from .modeladmin_mixins import ModelAdminMixin
from ..models import Week2, FluconazoleMissedDoses, AmphotericinMissedDoses, SignificantDiagnoses


class SignificantDiagnosesInline(TabularInlineMixin, admin.TabularInline):

    model = SignificantDiagnoses
    form = SignificantDiagnosesForm
    extra = 1


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

    inlines = [SignificantDiagnosesInline, FluconazoleMissedDosesInline,
               AmphotericinMissedDosesInline]

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
                'ampho_start_date',
                'ampho_end_date',
                'flucon_start_date',
                'flucon_stop_date',
                'flucy_start_date',
                'flucy_stop_date',
                'ambi_start_date',
                'ambi_stop_date',
                'other_drug',
                'other_drug_other',
                'antibiotic',
                'antibiotic_other',
                'blood_received',
                'units')}
         ],
        ['Clinical Assessment', {
            'fields': (
                'headache',
                'glasgow_coma_score',
                'confusion',
                'recent_seizure_less_72',
                'cn_palsy',
                'behaviour_change',
                'focal_neurology',
                'weight',
                'medicines',
                'medicine_other',
            )}
         ],
        #         ['Missed Doses', {
        #             'fields': (
        #                 'flucon_missed_doses',
        #                 'amphotericin_missed_doses')}
        #          ],
        audit_fieldset_tuple
    )

    radio_fields = {
        'discharged': admin.VERTICAL,
        'died': admin.VERTICAL,
        'flucon_missed_doses': admin.VERTICAL,
        'amphotericin_missed_doses': admin.VERTICAL,
        'blood_received': admin.VERTICAL,
        'headache': admin.VERTICAL,
        'recent_seizure_less_72': admin.VERTICAL,
        'behaviour_change': admin.VERTICAL,
        'confusion': admin.VERTICAL,
        'cn_palsy': admin.VERTICAL,
        'focal_neurology': admin.VERTICAL,
    }
    filter_horizontal = ('antibiotic', 'medicines', 'other_drug')
