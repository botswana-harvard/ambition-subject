from django.core.exceptions import ObjectDoesNotExist

from .models import SubjectLocator


def verify_subject_locator(subject_identifier=None):

    message = None
    try:
        SubjectLocator.objects.get(subject_identifier=subject_identifier)
    except ObjectDoesNotExist:
        message = ('Please complete the subject locator form before'
                   ' collecting any clinical data.')
    return message
