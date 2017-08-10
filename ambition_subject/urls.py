import sys

from django.conf.urls import url

from .admin_site import ambition_subject_admin
# from .load_randomization import load_randomization
#
# if 'migrate' not in sys.argv and 'makemigrations' not in sys.argv:
#     load_randomization()

urlpatterns = [
    url(r'^admin/', ambition_subject_admin.urls),
]
