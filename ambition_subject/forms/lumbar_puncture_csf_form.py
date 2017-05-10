from ..models import LumbarPunctureCsf
from .form_mixins import SubjectModelFormMixin
from edc_constants.constants import YES


class LumbarPunctureCSFForm(SubjectModelFormMixin):
    
    def clean(self):
        
        self.required_if(YES, field='csf_culture',
                         field_required='other_csf_culture')

    class Meta:
        model = LumbarPunctureCsf
        fields = '__all__'
