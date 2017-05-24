from .model_mixins import CrfModelMixin, ClinicalAssessment


class Week4(ClinicalAssessment, CrfModelMixin):

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
