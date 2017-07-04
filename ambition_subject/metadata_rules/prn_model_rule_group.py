from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import CrfRule
from edc_metadata.rules.crf import CrfRuleGroup
from edc_metadata.rules.decorators import register
from edc_metadata.rules.predicate import P


@register()
class PrnModelCrfRuleGroup(CrfRuleGroup):

    adverse_event = CrfRule(
        predicate=P('adverse_event', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['adverseevent'])

    microbiology = CrfRule(
        predicate=P('microbiology', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['microbiology'])

    radiology = CrfRule(
        predicate=P('radiology', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['radiology'])

    recurrence_symptom = CrfRule(
        predicate=P('recurrence_symptom', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['recurrencesymptom'])

    protocol_deviation = CrfRule(
        predicate=P('protocol_deviation', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['protocoldeviationviolation'])

    class Meta:
        app_label = 'ambition_subject'
        source_model = 'ambition_subject.prnmodel'
