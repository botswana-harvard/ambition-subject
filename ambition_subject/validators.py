from django.core.validators import RegexValidator


bp_validator = RegexValidator(
    '^\d{1,3}\/\d{1,3}$', message='Enter a valid BP in SYS/DIA format')

hm_validator = RegexValidator(
    '^([0-1]?\d|2[0-3])(?::([0-5]?\d))?(?::([0-5]?\d))?$',
    message='Enter a valid time in hour:minutes format')
