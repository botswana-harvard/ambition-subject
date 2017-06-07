from edc_model_wrapper import ModelWrapper

from ...models import SubjectVisit


class SubjectVisitModelWrapper(ModelWrapper):

    model = SubjectVisit
    url_namespace = 'ambition_subject'
    next_url_attrs = ['appointment']
    querystring_attrs = ['subject_identifier']

    @property
    def appointment(self):
        return self.object.subject_visit.appointment
