from django.test import TestCase, tag

from model_mommy import mommy

from ..identifiers import ScreeningIdentifier, AeIdentifier
from ..models import IdentifierHistory
from django.core.exceptions import ObjectDoesNotExist


class TestIdentifiers(TestCase):

    def test_identifier(self):
        identifier = ScreeningIdentifier()
        self.assertTrue(identifier.identifier)
        self.assertTrue(identifier.identifier.startswith('S'))

    def test_identifier_history(self):
        identifier = ScreeningIdentifier()
        try:
            IdentifierHistory.objects.get(identifier=identifier.identifier)
        except IdentifierHistory.DoesNotExist:
            self.fail('IdentifierHistory.DoesNotExist unexpectedly raised.')

    def test_model_allocates_identifier(self):
        obj = mommy.make_recipe('ambition_subject.subjectscreening')
        self.assertIsNotNone(obj.screening_identifier)
        self.assertTrue(obj.screening_identifier.startswith('S'))

    def test_tracking_identifier(self):
        identifiers = []
        for _ in range(0, 10):
            identifier = AeIdentifier()
            self.assertTrue(identifier.identifier)
            self.assertTrue(identifier.identifier.startswith('AE'))
            self.assertNotIn(identifier.identifier, identifiers)
            try:
                IdentifierHistory.objects.get(
                    identifier=identifier.identifier)
            except ObjectDoesNotExist:
                self.fail('ObjectDoesNotExist unexpectedly raised.')
            identifiers.append(identifier.identifier)
