from edc_visit_schedule.constants import DAYS, WEEKS
from edc_visit_schedule.schedule import Schedule

from .crfs import (
    crfs_d5, crfs_d1, crfs_d3, crfs_d7, crfs_d10, crfs_d12, crfs_d14,
    crfs_w4, crfs_w6, crfs_w8, crfs_w10)
from .requisitions import requisitions, requisitions_d1, requisitions_d3, requisitions_d7

# schedule for new participants
schedule1 = Schedule(name='schedule1', title='Ambition')

schedule1.add_visit(
    code='1000',
    title='Day 1',
    timepoint=0,
    base_interval=0,
    base_interval_unit=DAYS,
    requisitions=requisitions_d1,
    crfs=crfs_d1)

schedule1.add_visit(
    code='1003',
    title='Day 3',
    timepoint=1,
    base_interval=3,
    base_interval_unit=DAYS,
    requisitions=requisitions_d3,
    crfs=crfs_d3)

schedule1.add_visit(
    code='1005',
    title='Day 5',
    timepoint=2,
    base_interval=5,
    base_interval_unit=DAYS,
    requisitions=requisitions_d3,
    crfs=crfs_d5)

schedule1.add_visit(
    code='1007',
    title='Day 7',
    timepoint=3,
    base_interval=7,
    base_interval_unit=DAYS,
    requisitions=requisitions_d7,
    crfs=crfs_d7)

schedule1.add_visit(
    code='1010',
    title='Day 10',
    timepoint=4,
    base_interval=9,  # TODO: Base interval should be 10
    base_interval_unit=DAYS,
    requisitions=requisitions_d3,
    crfs=crfs_d10)

schedule1.add_visit(
    code='1012',
    title='Day 12',
    timepoint=5,
    base_interval=12,
    base_interval_unit=DAYS,
    requisitions=requisitions_d3,
    crfs=crfs_d12)

schedule1.add_visit(
    code='1014',
    title='Day 14',
    timepoint=6,
    base_interval=14,
    base_interval_unit=DAYS,
    requisitions=requisitions_d7,
    crfs=crfs_d14)

schedule1.add_visit(
    code='1028',
    title='Week 4',
    timepoint=7,
    base_interval=4,
    base_interval_unit=WEEKS,
    requisitions=requisitions,
    crfs=crfs_w4)

schedule1.add_visit(
    code='1042',
    title='Week 6',
    timepoint=8,
    base_interval=6,
    base_interval_unit=WEEKS,
    requisitions=requisitions,
    crfs=crfs_w6)

schedule1.add_visit(
    code='1056',
    title='Week 8',
    timepoint=9,
    base_interval=8,
    base_interval_unit=WEEKS,
    requisitions=requisitions,
    crfs=crfs_w8)

schedule1.add_visit(
    code='1070',
    title='Week 10',
    timepoint=10,
    base_interval=10,
    base_interval_unit=WEEKS,
    requisitions=requisitions,
    crfs=crfs_w10)
