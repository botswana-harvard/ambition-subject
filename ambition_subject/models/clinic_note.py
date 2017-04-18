from django.db import models
from .model_mixins import CrfModelMixin


class ClinicNote(CrfModelMixin):

    comments = models.CharField(
        verbose_name='Patient review',
        max_length=2000,
        help_text=''
    )
