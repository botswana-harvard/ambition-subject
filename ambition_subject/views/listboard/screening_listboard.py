# import re

from django.contrib.auth.decorators import login_required
# from django.db.models import Q
from django.utils.decorators import method_decorator

from ...models import SubjectScreening
from ..wrappers import SubjectScreeningModelWrapper
from .base_listboard import BaseListboardView


class ScreeningListboard(BaseListboardView):

    model = SubjectScreening
    model_wrapper_class = SubjectScreeningModelWrapper

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('screening_identifier'):
            options.update(
                {'screening_identifier': kwargs.get('screening_identifier')})
        return options
