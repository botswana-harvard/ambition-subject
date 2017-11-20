from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Ambition Subject'
    site_header = 'Ambition Subject'
    index_title = 'Ambition Subject'
    site_url = '/administration/'


ambition_subject_admin = AdminSite(name='ambition_subject_admin')
