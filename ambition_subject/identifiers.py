from edc_identifier.simple_identifier import SimpleUniqueIdentifier, SimpleTimestampIdentifier


class ScreeningIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'screening_identifier'
    template = 'S{device_id}{random_string}'
    model = 'ambition_subject.identifierhistory'


class AeIdentifier(SimpleUniqueIdentifier):
    random_string_length = 2
    identifier_type = 'ae_identifier'
    template = 'AE{device_id}{timestamp}{random_string}'
    identifier_cls = SimpleTimestampIdentifier