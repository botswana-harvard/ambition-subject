import os

from pathlib import PurePath

from .settings import BASE_DIR
from .models import RandomizationItem


def load_randomization():

    f = open(os.path.join(
        str(PurePath(BASE_DIR).parent),
        'ambition-subject',
        'ambition_test_randomization.csv'))
    for index, line in enumerate(f.readlines()):
        if index == 0:
            continue
        seq, drug_assignment, site = line.split(',')
        RandomizationItem.objects.get_or_create(
            name=seq, field_name=drug_assignment, display_index=site)
