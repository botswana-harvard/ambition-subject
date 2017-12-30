from ambition_rando.tests import SiteTestCaseMixin
from django.test import TestCase, tag
from edc_reference.site import site_reference_configs


class TestReference(SiteTestCaseMixin, TestCase):

    def test_(self):
        site_reference_configs.check()
