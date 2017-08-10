from django.conf.urls import url
from django.views.generic.base import RedirectView

from .admin_site import ambition_subject_admin

app_name = 'ambition_subject'

urlpatterns = [
    url(r'^admin/', ambition_subject_admin.urls),
    url(r'', RedirectView.as_view(url='/'), name='home_url'),
]
