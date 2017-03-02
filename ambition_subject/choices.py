
from django.utils.translation import ugettext as _

from edc_constants.constants import OTHER

VISIT_UNSCHEDULED_REASON = (
    ('Routine oncology',
     _('Routine oncology clinic visit (i.e. planned chemo, follow-up)')),
    ('Ill oncology', _('Ill oncology clinic visit')),
    ('Patient called', _('Patient called to come for visit')),
    (OTHER, _('Other, specify:')),
)
