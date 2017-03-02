from edc_lab import AliquotType, LabProfile, ProcessingProfile, RequisitionPanel
from edc_lab.site_labs import site_labs


lab_profile = LabProfile('ambition_subject')

pl = AliquotType('Plasma', 'PL', '36')
lab_profile.add_aliquot_type(pl)

bc = AliquotType('Buffy Coat', 'BC', '12')
lab_profile.add_aliquot_type(bc)

wb = AliquotType('Whole Blood', 'WB', '02')
wb.add_derivative(bc)
wb.add_derivative(pl)
lab_profile.add_aliquot_type(wb)

viral_load_panel = RequisitionPanel('viral_load', wb, abbreviation='VLD')
viral_load_processing = ProcessingProfile('viral_load', wb)
viral_load_processing.add_process(pl, 3)
viral_load_processing.add_process(bc, 1)
viral_load_panel.processing_profile = viral_load_processing
lab_profile.add_processing_profile(viral_load_processing)
lab_profile.add_panel(viral_load_panel)


site_labs.register('ambition_subject.subjectrequisition', lab_profile)
