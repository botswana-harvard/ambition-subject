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

    protocol_deviation = CrfRule(
        predicate=P('protocol_deviation', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['protocoldeviationviolation'])

    lumbar_puncture = CrfRule(
        predicate=P('lumbar_puncture', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['lumbarpuncturecsf'])

    death_report = CrfRule(
        predicate=P('death_report', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['deathreport'])

    class Meta:
        app_label = 'ambition_subject'
        source_model = 'ambition_subject.prnmodel'
