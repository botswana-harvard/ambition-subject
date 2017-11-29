from edc_base.preload_data import PreloadData
from edc_constants.constants import OTHER, UNKNOWN, NORMAL

from .constants import HEADACHE, VISUAL_LOSS

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
    'ambition_subject.antibiotic': [
        ('flucloxacillin', 'Flucloxacillin'),
        ('gentamicin', 'Gentamicin'),
        ('ceftriaxone', 'Ceftriaxone'),
        ('amoxicillin_ampicillin', 'Amoxicillin/Ampicillin'),
        ('doxycycline', 'Doxycycline'),
        ('erythromycin', 'Erythromycin'),
        ('ciprofloxacin', 'Ciprofloxacin'),
        (OTHER, 'Other, specify')
    ],
    'ambition_subject.antibiotictreatment': [
        ('amoxicillin', 'Amoxicillin'),
        ('flucloxacillin', 'Flucloxacillin'),
        ('doxycycline', 'Doxycycline'),
        ('ceftriaxone', 'Ceftriaxone'),
        ('erythromycin', 'Erythromycin'),
        ('ciprofloxacin', 'Ciprofloxacin'),
        (OTHER, 'Other, specify')
    ],
    'ambition_subject.day14medication': [
        ('fluconazole', 'Fluconazole'),
        ('rifampicin', ' Rifampicin'),
        ('co_trimoxazole', 'Co-trimoxazole'),
        (OTHER, 'Other')
    ],
    'ambition_subject.meningitissymptom': [
        ('headache', 'Headache'),
        ('vomiting', 'Vomiting'),
        ('fever', 'Fever'),
        ('seizures', 'Seizures'),
        ('neck_pain', 'Neck Pain'),
        (OTHER, 'Other')
    ],
    'ambition_subject.missedvisitreason': [
        ('transportation_difficulty', 'Transportation difficulty'),
        ('severely_sick', 'Severely sick or other physical conditions'),
        ('discouraged_by_clinic_situation', 'Discouraged by clinic situation '
                                            '(long waits, rude clinicians)'),
        ('away_working_schooling', 'Away Working/Schooling'),
        ('away_visiting', 'Away Visiting'),
        ('forgot', 'Forgot about appointment for clinic visit'),
        ('not_given_an_appointment', 'Not given an appointment'),
        (OTHER, 'Other, specify;'),
        (UNKNOWN, 'Reason not known at time of completing this form')
    ],
    'ambition_subject.medication': [
        ('TMP-SMX', 'TMP-SMX'),
        (OTHER, 'Other, specify;')
    ],
    'ambition_subject.neurological': [
        ('meningism', 'Meningism'),
        ('papilloedema', ' Papilloedema'),
        ('focal_neurologic_deficit', 'Focal neurologic deficit'),
        ('CN_VI_palsy', 'Cranial Nerve VI palsy'),
        ('CN_III_palsy', 'Cranial Nerve III palsy'),
        ('CN_IV_palsy', 'Cranial Nerve IV palsy'),
        ('CN_VII_palsy', 'Cranial Nerve VII palsy'),
        ('CN_VIII_palsy', 'Cranial Nerve VIII palsy'),
        (OTHER, 'Other CN palsy'),
    ],
    'ambition_subject.otherdrug': [
        ('potassium', ' Potassium'),
        ('magnesium', 'Magnesium'),
        ('vitamins', ' Vitamins'),
        ('tmp_smx_Cotrimoxazole', ' TMP-SMX/Cotrimoxazole'),
        ('anti_convulsants', 'Anti convulsants'),
        ('antibiotics', 'Antibiotics'),
        (OTHER, 'Other, specify')
    ],
    'ambition_subject.significantnewdiagnosis': [
        ('tb_pulmonary', 'TB pulmonary'),
        ('kaposi_sarcoma', 'Kaposi’s sarcoma'),
        ('bacteraemia', 'Bacteraemia'),
        ('diarrhoeal_wasting', 'Diarrhoeal wasting'),
        ('tb_extra_pulmonary', 'TB extra-pulmonary'),
        ('malaria', 'Malaria'),
        ('bacterial_pneumonia', 'Bacterial pneumonia'),
        (OTHER, 'Other, please specify:'),
    ],
    'ambition_subject.symptom': [
        ('cough', 'Cough'),
        (HEADACHE, 'Headache'),
        ('double_vision', 'Double vision'),
        (VISUAL_LOSS, 'Visual loss'),
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
        ('skin_lesions', 'Skin Lesions'),
        ('shortness_of_breath', 'Shortness of breath'),
    ],
    'ambition_subject.abnormalresultsreason': [
        ('cerebral_oedema', 'Cerebral oedema'),
        ('hydrocephalus', 'Hydrocephalus'),
        ('cryptococcomas', 'Cryptococcomas'),
        ('dilated_virchow_robin_spaces', 'Dilated Virchow robin spaces'),
        ('enhancing_mass_lesions',
         'Enhancing mass lesions DD Toxoplasmosis, TB, lymphoma'),
        ('infarcts', 'Infarcts'),
        (OTHER, 'Other'),
    ],
    'ambition_subject.cxrtype': [
        (NORMAL, 'Normal'),
        ('hilar_adenopathy', 'Hilar adenopathy'),
        ('miliary_appearance', 'Miliary appearance'),
        ('pleural_effusion', 'Pleural effusion'),
        ('infiltrates', 'Infiltrates'),
    ],
    'ambition_subject.infiltratelocation': [
        ('lul', 'LUL'),
        ('lll', 'LLL'),
        ('rul', 'RUL'),
        ('rll', 'RLL'),
        ('rml', 'RML'),
        ('diffuse', 'Diffuse'),
    ],
}

model_data = {
    'edc_lab.consignee': {
        'name': 'Botswana-Harvard Partnership',
        'contact_name': 'Dr Sikhulile Moyo',
        'address': 'Private Bag BO 320, Bontleng',
        'postal_code': 'Plot 1836, Gaborone',
        'city': 'Gaborone',
        'state': '',
        'country': 'Botswana',
        'telephone': '+267 3902671',
        'mobile': '',
        'fax': '+267 3901284',
        'email': ''}
}

unique_field_data = {
    'edc_lab.consignee': {
        'name': ('Botswana-Harvard Partnership',
                 'Botswana-Harvard AIDS Institute Partnership')
    }
}

preload_data = PreloadData(
    list_data=list_data,
    model_data=model_data,
    unique_field_data=unique_field_data)
