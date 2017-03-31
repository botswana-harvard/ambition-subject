from .form_mixins import SubjectModelFormMixin

from ..models import LumbarPunctureCerebroSpinalFluid


class LumbarPunctureCerebroSpinalFluidForm(SubjectModelFormMixin):

    class Meta():
        model = LumbarPunctureCerebroSpinalFluid
        fields = '__all__'
