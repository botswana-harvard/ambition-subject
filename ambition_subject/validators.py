from django.core.validators import RegexValidator


bp_validator = RegexValidator(
    '^\d{1,3}\/\d{1,3}$', message='Enter a valid BP in SYS/DIA format')

hm_validator = RegexValidator(
    '^([0-9]{1,3}:[0-5][0-9])$',
    message='Enter a valid time in hour:minutes format')
