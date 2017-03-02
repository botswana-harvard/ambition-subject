from edc_visit_schedule.schedule import Schedule

from .crfs import crfs
from .requisitions import requisitions

# schedule for new participants
schedule = Schedule(name='schedule', title='Ambition')

schedule.add_visit(
    code='A0',
    title='Visit Schedule',
    timepoint=0,
    base_interval=0,
    requisitions=requisitions,
    crfs=crfs)
