from edc_prn import CrfPrn, Prn, site_prn_forms, AlreadyRegistered

from .admin_site import ambition_subject_admin

prn_models = [
    'ambition_subject.protocoldeviationviolation',
    'ambition_subject.studyterminationconclusion',
]

crf_prn_models = [
    'ambition_subject.recurrencesymptom',
]

for model in prn_models:
    prn = Prn(
        model=model,
        url_namespace=ambition_subject_admin.name)
    try:
        site_prn_forms.register(prn)
    except AlreadyRegistered:
        pass

for model in crf_prn_models:
    prn = CrfPrn(
        model=model,
        url_namespace=ambition_subject_admin.name)
    site_prn_forms.register(prn)
