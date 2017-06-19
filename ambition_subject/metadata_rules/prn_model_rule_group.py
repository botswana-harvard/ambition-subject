from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules.crf_rule import CrfRule
from edc_metadata.rules.decorators import register
from edc_metadata.rules.logic import Logic
from edc_metadata.rules.predicate import P
from edc_metadata.rules.rule_group import RuleGroup


@register()
class PrnModelRuleGroup(RuleGroup):

    adverse_event = CrfRule(
        logic=Logic(
            predicate=P('adverse_event', 'eq', YES),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_models=['adverseevent'])

    microbiology = CrfRule(
        logic=Logic(
            predicate=P('microbiology', 'eq', YES),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_models=['microbiology'])

    radiology = CrfRule(
        logic=Logic(
            predicate=P('radiology', 'eq', YES),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_models=['radiology'])

    recurrence_symptom = CrfRule(
        logic=Logic(
            predicate=P('recurrence_symptom', 'eq', YES),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_models=['recurrencesymptom'])

    protocol_deviation = CrfRule(
        logic=Logic(
            predicate=P('protocol_deviation', 'eq', YES),
            consequence=REQUIRED,
            alternative=NOT_REQUIRED),
        target_models=['protocoldeviationviolation'])

    class Meta:
        app_label = 'ambition_subject'
        source_model = 'ambition_subject.prnmodel'
