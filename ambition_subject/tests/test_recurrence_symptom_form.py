from django.test import TestCase
from model_mommy import mommy 
 
from edc_base.utils import get_utcnow
from edc_visit_tracking.constants import SCHEDULED
from edc_constants.constants import NO, YES, OTHER

from ..models import RecurrenceSymptom
 
from ..forms import RecurrenceSymptomForm


class TestRecurrenceSymptomForm(TestCase):
    
    def setUp(self):
        self.meningitissymptom = mommy.make_recipe('ambition_subject.meningitissymptom')
        self.neurological = mommy.make_recipe('ambition_subject.neurological')
            
    def test_valid_form(self):
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower)
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
        
    def test_meningitis_symptom_choice_other(self):
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,)
        data = obj.__dict__
        data.update({'meningitis_symptom':[self.meningitissymptom.id],
                     'neurological':[self.neurological.id],
                     'meningitis_symptom_other':None})
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())
           
    def test_meningitis_symptom_choice_available(self):
        """
        Assert meningitis symtom choice is not other
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   meningitis_symptom= None)
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())
          
    def test_if_has_focal_neurologic_deficit(self):
        """
        Assert that participant has focal neurological deficit
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   neurological=YES)
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
          
    def test_if_neurologic_not_given(self):
        """
        Assert that neurologic is not offered
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   neurologic=OTHER),
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
          
    def test_if_amb_administered(self):
        """
        Assert that amb is administered
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   amb_administered=YES)
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
          
    def test_if_steroids_administered(self):
        """
        Assert that steroids is administered
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   steroids_administered=YES)
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
          
    def test_if_steroids_administered_choice_is_other(self):
        """
        Assert that the choice for the steroids administered is other
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   steroids_administered=OTHER)
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
          
    def test_if_antibiotic_treatment_choice_is_other(self):
        """
        Assert that the choice for the antibiotic treatment choice is other
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   antibiotic_treatment='oral_prednisolone')
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
          
    def test_if_participant_taking_arv(self):
        """
        Assert that participant is on ARV
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   on_arvs=YES)
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
          
    def test_if_erythromicin_given(self):
        """
        Assert the participant is never given Erythromicin
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   antibiotic_treatment=NO)
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
          
    def test_if_ciprofloxacin_given(self):
        """
        Assert the participant is never given Ciprofloxacin
        """
        obj = mommy.prepare_recipe(RecurrenceSymptom._meta.label_lower,
                                   antibiotic_treatment=NO)
        form = RecurrenceSymptomForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
