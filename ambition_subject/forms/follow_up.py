from .form_mixins import SubjectModelFormMixin

from ..models import FollowUp


class FollowUpForm(SubjectModelFormMixin):

    class Meta():
        model = FollowUp
        fields = '__all__'
