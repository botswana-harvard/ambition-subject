from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from edc_constants.constants import OTHER

list_data = {
    'ambition_subject.adverse_event': [
        ('Anaemia', 'Anaemia'),
        ('Thrombocytopenia', 'Thrombocytopenia'),
        ('Diarrhoea', 'Diarrhoea'),
        ('Thrombophlebitis', 'Renal impairment'),
        ('Pneumonia', 'Pneumonia'),
        ('TB', 'TB'),
        ('Hypokalaemia', 'Hypokalaemia'),
        ('Bacteraemia/sepsis', 'Bacteraemia/sepsis'),
        ('Neutropaenia', 'Neutropaenia'),
        ('CM IRIS', 'CM IRIS')
        ('Respiratory distress', 'Respiratory distress'),
        (OTHER, 'Other')
    ],
    'ambition_subject.symptoms': [
        ('Headache', 'Headache'),
        ('Double vision', 'Double vision'),
        ('Visual loss', 'Visual loss'),
        ('Fever', 'Fever'),
        ('Hearing loss', 'Hearing loss'),
        ('Confusion', 'Confusion'),
        ('Drowsiness', 'Drowsiness'),
        ('Behaviour change', 'Behaviour change'),
        ('Focal weakness', 'Focal weakness'),
        ('Seizures (<72 hrs)', 'Seizures (<72 hrs)'),
        ('Seizures (72 hrs - 1 mo)', 'Seizures (72 hrs - 1 mo)'),
        ('Nausea', 'Nausea'),
        ('Vomiting', 'Vomiting'),
        ('Weight Loss', 'Weight Loss'),
        ('Skin Lesions Cough', 'Skin Lesions Cough'),
        ('Shortness of breath', 'Shortness of breath'),
    ],
    'ambition_subject.neurological': [
        ('Meningismus', 'Meningismus'),
        ('Papilloedema', 'Papilloedema'),
        ('Focal neurologic deficit', 'Focal neurologic deficit'),
        ('Cranial Nerve VI palsy', 'Cranial Nerve VI palsy'),
        ('Cranial Nerve III palsy', 'Cranial Nerve III palsy'),
        ('Cranial Nerve IV palsy', 'Cranial Nerve IV palsy'),
        ('Cranial Nerve VII palsy', 'Cranial Nerve VII palsy'),
        ('Cranial Nerve VIII palsy', 'Cranial Nerve VIII palsy'),
        (OTHER, 'Other CN palsy'), ],
}


for list_obj in list_data.keys():
    try:
        model = django_apps.get_app_config(
            list_obj.split('.')[0]).get_model(list_obj.split('.')[1])
        for tpl in list_data.get(list_obj):
            short_name, display_value = tpl
            try:
                obj = model.objects.get(short_name=short_name)
            except ObjectDoesNotExist:
                model.objects.create(short_name=short_name, name=display_value)
            else:
                obj.name = display_value
                obj.save()
    except Exception as e:
        print(e)
