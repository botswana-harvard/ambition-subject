from django.db import models


class DisenrollmentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier,
                           visit_schedule_name, schedule_name):
        return self.get(
            subject_identifier=subject_identifier,
            visit_schedule_name=visit_schedule_name,
            schedule_name=schedule_name)


class EnrollmentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier,
                           visit_schedule_name, schedule_name):
        return self.get(
            subject_identifier=subject_identifier,
            visit_schedule_name=visit_schedule_name,
            schedule_name=schedule_name
        )


class SubjectConsentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version,
        )
