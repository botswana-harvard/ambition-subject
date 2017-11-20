from django.contrib import admin

from edc_model_admin import audit_fieldset_tuple


class BaseDeathReportTmg(admin.ModelAdmin):

    fieldsets = (
        ('Opinion of TMG', {
            'fields': (
                'subject_visit',
                'cause_of_death',
                'cause_of_death_other',
                'tb_site',
                'cause_of_death_agreed')}),
        ('Summary', {
            'fields': (
                'death_narrative',)}),
        audit_fieldset_tuple
    )

    radio_fields = {
        'cause_of_death': admin.VERTICAL,
        'cause_of_death_agreed': admin.VERTICAL,
        'tb_site': admin.VERTICAL}
