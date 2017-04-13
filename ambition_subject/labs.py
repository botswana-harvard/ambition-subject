from edc_lab import AliquotType, LabProfile, ProcessingProfile, RequisitionPanel
from edc_lab.site_labs import site_labs


lab_profile = LabProfile('ambition_subject')

pl = AliquotType('Plasma', 'PL', '36')
lab_profile.add_aliquot_type(pl)

bc = AliquotType('Buffy Coat', 'BC', '12')
lab_profile.add_aliquot_type(bc)

serum = AliquotType('Serum', 'SERUM', '06')
lab_profile.add_aliquot_type(serum)

# TODO: Get correct sample codes from LIS
fbc = AliquotType('FBC', 'FBC', '63')
lab_profile.add_aliquot_type(fbc)

# # TODO: Get correct sample codes from LIS
# chemistry = AliquotType('Chemistry', 'CHEM' '59')
# lab_profile.add_aliquot_type(chemistry)

wb = AliquotType('Whole Blood', 'WB', '02')
wb.add_derivative(bc)
wb.add_derivative(pl)
wb.add_derivative(serum)
wb.add_derivative(fbc)
lab_profile.add_aliquot_type(wb)

# TODO: Get correct sample codes from LIS
qfc = AliquotType('Quantitative Fungal Culture', 'QFC', '61')

# TODO: Get correct sample codes from LIS
csf_store = AliquotType('CSF STORE', 'CSF STORE', '62')

# TODO: Get correct sample codes from LIS
csf = AliquotType('Cerebro Spinal Fluid', 'csf', '56')
csf.add_derivative(qfc)
csf.add_derivative(csf_store)

csf_panel = RequisitionPanel('Spinal Fluid', csf, abbreviation='CSF')
csf_processing = ProcessingProfile('spinal_fluid', csf)
csf_processing.add_process(qfc, 10)
csf_processing.add_process(csf_store, 1)
csf_panel.processing_profile = csf_processing
lab_profile.add_processing_profile(csf_processing)
lab_profile.add_panel(csf_panel)

viral_load_panel = RequisitionPanel('Viral Load', wb, abbreviation='VLD')
viral_load_processing = ProcessingProfile('viral_load', wb)
viral_load_processing.add_process(pl, 3)
viral_load_processing.add_process(bc, 1)
viral_load_panel.processing_profile = viral_load_processing
lab_profile.add_processing_profile(viral_load_processing)
lab_profile.add_panel(viral_load_panel)

cd4_panel = RequisitionPanel('CD4', wb, abbreviation='CD4')
cd4_processing = ProcessingProfile('cd4', wb)
cd4_panel.processing_profile = cd4_processing
lab_profile.add_processing_profile(cd4_processing)
lab_profile.add_panel(cd4_panel)

fbc_panel = RequisitionPanel('Full Blood Count', wb, abbreviation='FBC')
fbc_processing = ProcessingProfile('fbc', wb)
fbc_panel.processing_profile = fbc_processing
lab_profile.add_processing_profile(fbc_processing)
lab_profile.add_panel(fbc_panel)

chemistry_alt_panel = RequisitionPanel('Creat, Urea, Elec, ALT', wb, abbreviation='CUEA')
chemistry_alt_processing = ProcessingProfile('chem + alt', wb)
chemistry_alt_panel.processing_profile = chemistry_alt_processing
lab_profile.add_processing_profile(chemistry_alt_processing)
lab_profile.add_panel(chemistry_alt_panel)

chemistry_panel = RequisitionPanel('Creat, Urea, Elec', wb, abbreviation='CUE')
chemistry_processing = ProcessingProfile('chem', wb)
chemistry_panel.processing_profile = chemistry_processing
lab_profile.add_processing_profile(chemistry_processing)
lab_profile.add_panel(chemistry_panel)

site_labs.register('ambition_subject.subjectrequisition', lab_profile)
