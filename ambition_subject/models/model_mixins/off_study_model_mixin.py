from decimal import Decimal
from django.apps import apps as django_apps
from edc_offstudy.model_mixins import OffstudyMixin as BaseOffstudyMixin, OffstudyError


class OffstudyModelMixin(BaseOffstudyMixin):

    def neutrophils_result(self, obj=None):
        """ if absolute_neutrophil < (0.5 x 109/L ) eq 54.5 then participant is
        ineligible, take offstudy.
        """
        neutrophils_allowed_limit = 0.5 * 109
        return (Decimal(obj.absolute_neutrophil or 0) <
                Decimal(neutrophils_allowed_limit))

    def platelets_result(self, obj=None):
        """ if  platelets < (50 x 109/L) then participant is ineligible.
        take offstudy.
        """
        platelets_allowed_limit = 50 * 109
        return (Decimal(obj.platelets or 0) <
                Decimal(platelets_allowed_limit))

    def alt_result(self, obj=None):
        """ if  ALT > 200 IU/mL then participant is ineligible.
        take offstudy.
        """
        return Decimal(obj.alt or 0) > Decimal('200')

    def is_eligible_after_blood_result(self):
        try:
            if not (self._meta.model_name == 'bloodresult' and
                    self.subject_visit.visit_code == '1000'):
                BloodResult = django_apps.get_app_config(
                    'ambition_subject').get_model('bloodresult')
                obj = BloodResult.objects.get(
                    subject_visit=self.subject_visit,
                    subject_visit__visit_code='1000')
                if any((self.neutrophils_result(obj=obj), self.platelets_result(obj=obj),
                        self.alt_result(obj=obj))):
                    return False
        except BloodResult.DoesNotExist or TypeError:
            return True
        return True

    def save(self, *args, **kwargs):
        if not self.is_eligible_after_blood_result():
            raise OffstudyError(
                'Participant was reported off study on \'{0}\'. '
                'Data reported after this date'
                ' cannot be captured.')
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        consent_model = None
