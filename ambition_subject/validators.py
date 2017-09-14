from django.core.validators import RegexValidator


bp_validator = RegexValidator(
    '^\d{1,3}\/\d{1,3}$', message='Enter a valid BP in SYS/DIA format')

hm_validator = RegexValidator(
    '^([0-9]{1,3}:[0-5][0-9])$',
    message='Enter a valid time in hour:minutes format')

span_validator = RegexValidator(
    '^(([1-9]day|([1-2][0-9]|3[0-1])days)|\/|([1-9]week|([1-4][0-9]|5[0-2])weeks)'
    '|\/|([1-9]month|1[0-2]months))$',
    message='Enter a valid duration in days/weeks/months')
