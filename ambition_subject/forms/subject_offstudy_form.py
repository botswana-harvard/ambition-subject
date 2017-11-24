from ambition_subject.models import SubjectOffstudy
from edc_offstudy.modelform_mixins import OffstudyModelFormMixin

from .form_mixins import SubjectModelFormMixin


class SubjectOffStudyForm (OffstudyModelFormMixin, SubjectModelFormMixin):

    class Meta:
        model = SubjectOffstudy
        fields = '__all__'
