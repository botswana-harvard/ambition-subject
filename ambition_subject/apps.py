from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'ambition_subject'
    listboard_template_name = 'ambition_subject/listboard.html'
    dashboard_template_name = 'ambition_subject/dashboard.html'
    base_template_name = 'edc_base/base.html'
    listboard_url_name = 'ambition_subject:listboard_url'
    dashboard_url_name = 'ambition_subject:dashboard_url'
    admin_site_name = 'ambition_subject_admin'

    def ready(self):
        from .models.signals import subject_consent_on_post_save
