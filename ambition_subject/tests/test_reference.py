from ambition_rando.tests import AmbitionTestCaseMixin
from django.test import TestCase, tag
from django.test.utils import override_settings
from edc_reference.site import site_reference_configs


@override_settings(SITE_ID='10')
class TestReference(AmbitionTestCaseMixin, TestCase):

    def test_(self):
        site_reference_configs.check()
