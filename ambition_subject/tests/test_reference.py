from ambition_rando.tests import AmbitionTestCaseMixin
from django.test import TestCase, tag
from edc_reference.site import site_reference_configs


class TestReference(AmbitionTestCaseMixin, TestCase):

    def test_(self):
        site_reference_configs.check()
