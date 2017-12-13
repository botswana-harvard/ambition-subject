from edc_fieldsets import Fieldset

from ...constants import DAY1, DAY7, DAY14, WEEK4, WEEK6, WEEK8, WEEK10

fs = {}
fields = [
    ('ALT', 'LFT', 'urea'),
    ('CD4', 'Immunology', None),
    ('vl', 'Immunology', None),
    ('creatinine', 'RFT', None),
    ('haemoglobin', 'CBC', None),
    ('magnesium', 'RFT', None),
    ('neutrophil', 'CBC', None),
    ('platelets', 'CBC', None),
    ('potassium', 'RFT', None),
    ('sodium', 'RFT', None),
    ('urea', 'RFT', None),
    ('wbc', 'CBC', None),
]
for field, label, insert_after in fields:
    fieldset = Fieldset(
        field, f'{field}_units', f'{field}_abnormal', f'{field}_reportable',
        section=f'{label}: {field.upper()}')
    fs.update({field: fieldset})

fs.update({'crag': Fieldset(
    'bios_crag',
    'crag_control_result',
    'crag_t1_result',
    'crag_t2_result',
    section='BIOSYNEX® CryptoPS (Semi-quantitative CrAg)')})

conditional_fieldsets = {
    DAY1: (
        fs.get('ALT'),
        fs.get('wbc'),
        fs.get('platelets'),
        fs.get('haemoglobin'),
        fs.get('neutrophil'),
        fs.get('CD4'),
        fs.get('vl'),
        fs.get('crag')),
    DAY7: (
        fs.get('ALT'),
        fs.get('wbc'),
        fs.get('platelets'),
        fs.get('haemoglobin'),
        fs.get('neutrophil')),
    DAY14: (
        fs.get('ALT'),
        fs.get('wbc'),
        fs.get('platelets'),
        fs.get('haemoglobin'),
        fs.get('neutrophil')),
    WEEK4: (
        fs.get('ALT'),
        fs.get('wbc'),
        fs.get('platelets'),
        fs.get('haemoglobin'),
        fs.get('neutrophil')),
    WEEK6: (
        fs.get('wbc'),
        fs.get('platelets'),
        fs.get('haemoglobin'),
        fs.get('neutrophil')),
    WEEK8: (
        fs.get('wbc'),
        fs.get('platelets'),
        fs.get('haemoglobin'),
        fs.get('neutrophil')),
    WEEK10: (
        fs.get('wbc'),
        fs.get('platelets'),
        fs.get('haemoglobin'),
        fs.get('neutrophil'))
}
