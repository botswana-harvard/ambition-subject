from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import CrfRule
from edc_metadata.rules.crf import CrfRuleGroup
from edc_metadata.rules.decorators import register
from edc_metadata.rules.predicate import P


@register()
class StudyTerminationConclusionCrfRuleGroup(CrfRuleGroup):

    protocol_deviation_violation = CrfRule(
        predicate=P('termination_reason', 'eq', 'included_in_error'),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=['protocoldeviationviolation'])

    class Meta:
        app_label = 'ambition_subject'
        source_model = 'ambition_subject.studyterminationconclusion'
