from edc_base.utils import get_utcnow

from edc_registration.models import RegisteredSubject

from .constants import RANDOMIZED
from .models import RandomizationItem, SubjectRandomization


class Randomization:

    def __init__(self, obj, randomization_datetime=None):
        randomization_datetime = randomization_datetime or get_utcnow()
        self.initials = None
        self.rx = None
        self.sid = None
        self.study_site = None
        registered_subject = RegisteredSubject.objects.get(
            subject_identifier=obj.subject_identifier)
        if SubjectRandomization.objects.filter(study_site=obj.study_site).count() == 0:
            next_to_pick = 1
        else:
            next_to_pick = SubjectRandomization.objects.filter(
                study_site=obj.study_site).order_by('-sid').first().sid + 1
        next_randomization_item = RandomizationItem.objects.get(
            name=str(next_to_pick), display_index=obj.study_site)

        SubjectRandomization.objects.get_or_create(
            study_site=next_randomization_item.display_index,
            sid=int(next_randomization_item.name),
            rx=next_randomization_item.field_name,
            subject_identifier=obj.subject_identifier,
            initials=obj.initials,
            randomization_datetime=randomization_datetime,
        )
        self.study_site = obj.study_site
        registered_subject.sid = self.sid
        registered_subject.randomization_datetime = randomization_datetime
        registered_subject.registration_status = RANDOMIZED
        registered_subject.modified = get_utcnow()
        registered_subject.save()
