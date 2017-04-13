from edc_visit_schedule.constants import DAYS, WEEKS
from edc_visit_schedule.schedule import Schedule

from .crfs import (
    crfs, day1_crfs, day3_crfs, day7_crfs, day14_crfs, week4_crfs, follow_up)
from .requisitions import requisitions, requisitions_d1, requisitions_d3, requisitions_d7

# schedule for new participants
schedule = Schedule(name='schedule', title='Ambition')

schedule.add_visit(
    code='D1',
    title='Day 1',
    timepoint=0,
    base_interval=1,
    base_interval_unit=DAYS,
    requisitions=requisitions_d1,
    crfs=day1_crfs)

schedule.add_visit(
    code='D3',
    title='Day 3',
    timepoint=1,
    base_interval=3,
    base_interval_unit=DAYS,
    requisitions=requisitions_d3,
    crfs=day3_crfs)

schedule.add_visit(
    code='D5',
    title='Day 5',
    timepoint=2,
    base_interval=5,
    base_interval_unit=DAYS,
    requisitions=requisitions_d3,
    crfs=crfs)

schedule.add_visit(
    code='D7',
    title='Day 7',
    timepoint=3,
    base_interval=7,
    base_interval_unit=DAYS,
    requisitions=requisitions_d7,
    crfs=day7_crfs)

schedule.add_visit(
    code='D10',
    title='Day 10',
    timepoint=4,
    base_interval=9, #TODO: Base interval should be 10
    base_interval_unit=DAYS,
    requisitions=requisitions_d3,
    crfs=crfs)

schedule.add_visit(
    code='D12',
    title='Day 12',
    timepoint=5,
    base_interval=12,
    base_interval_unit=DAYS,
    requisitions=requisitions_d3,
    crfs=crfs)

schedule.add_visit(
    code='D14',
    title='Day 14',
    timepoint=6,
    base_interval=14,
    base_interval_unit=DAYS,
    requisitions=requisitions_d7,
    crfs=day14_crfs)

schedule.add_visit(
    code='W4',
    title='Week 4',
    timepoint=7,
    base_interval=4,
    base_interval_unit=WEEKS,
    requisitions=requisitions,
    crfs=week4_crfs)

schedule.add_visit(
    code='W6',
    title='Week 6',
    timepoint=8,
    base_interval=6,
    base_interval_unit=WEEKS,
    requisitions=requisitions,
    crfs=follow_up)

schedule.add_visit(
    code='W8',
    title='Week 8',
    timepoint=9,
    base_interval=8,
    base_interval_unit=WEEKS,
    requisitions=requisitions,
    crfs=follow_up)

schedule.add_visit(
    code='W10',
    title='Week 10',
    timepoint=10,
    base_interval=10,
    base_interval_unit=WEEKS,
    requisitions=requisitions,
    crfs=follow_up)
