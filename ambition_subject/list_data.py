from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from edc_constants.constants import OTHER

list_data = {
    'ambition_subject.aeclassification': [
        ('anaemia', 'Anaemia'),
        ('thrombocytopenia', 'Thrombocytopenia'),
        ('diarrhoea', 'Diarrhoea'),
        ('thrombophlebitis', 'Renal impairment'),
        ('pneumonia', 'Pneumonia'),
        ('TB', 'TB'),
        ('hypokalaemia', 'Hypokalaemia'),
        ('bacteraemia/sepsis', 'Bacteraemia/sepsis'),
        ('neutropaenia', 'Neutropaenia'),
        ('CM_IRIS', 'CM IRIS'),
        ('respiratory_distress', 'Respiratory distress'),
        (OTHER, 'Other')
    ],
    'ambition_subject.symptoms': [
        ('headache', 'Headache'),
        ('double_vision', 'Double vision'),
        ('visual_loss', 'Visual loss'),
        ('fever', 'Fever'),
        ('hearing_loss', 'Hearing loss'),
        ('confusion', 'Confusion'),
        ('drowsiness', 'Drowsiness'),
        ('behaviour_change', 'Behaviour change'),
        ('focal_weakness', 'Focal weakness'),
        ('seizures_lt_72 hrs', 'Seizures (<72 hrs)'),
        ('seizures_gt_72', 'Seizures (72 hrs - 1 mo)'),
        ('nausea', 'Nausea'),
        ('vomiting', 'Vomiting'),
        ('weight_loss', 'Weight Loss'),
        ('skin_lesions_cough', 'Skin Lesions Cough'),
        ('shortness_of_breath', 'Shortness of breath'),
    ],
    'ambition_subject.neurological': [
        ('meningismus', 'Meningismus'),
        ('papilloedema', 'Papilloedema'),
        ('focal_neurologic_deficit', 'Focal neurologic deficit'),
        ('CN_VI_palsy', 'Cranial Nerve VI palsy'),
        ('CN_III_palsy', 'Cranial Nerve III palsy'),
        ('CN_IV_palsy', 'Cranial Nerve IV palsy'),
        ('CN_VII_palsy', 'Cranial Nerve VII palsy'),
        ('CN_VIII_palsy', 'Cranial Nerve VIII palsy'),
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
