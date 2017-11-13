from ambition_subject.models import SubjectOffstudy
from edc_offstudy.modelform_mixins import OffStudyFormMixin

from .form_mixins import SubjectModelFormMixin


class SubjectOffStudyForm (OffStudyFormMixin, SubjectModelFormMixin):

    class Meta:
        model = SubjectOffstudy
        fields = '__all__'
