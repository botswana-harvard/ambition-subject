from edc_lab import AliquotType, LabProfile, ProcessingProfile, RequisitionPanel
from edc_lab.site_labs import site_labs
from edc_lab.lab.processing_profile import Process


lab_profile = LabProfile(
    name='ambition_subject')

pl = AliquotType(name='Plasma', alpha_code='PL', numeric_code='36')

bc = AliquotType(name='Buffy Coat', alpha_code='BC', numeric_code='12')

serum = AliquotType(name='Serum', alpha_code='SERUM', numeric_code='06')

# TODO: Get correct sample codes from LIS
fbc = AliquotType(name='FBC', alpha_code='FBC', numeric_code='63')

# # TODO: Get correct sample codes from LIS
# chemistry = AliquotType('Chemistry', 'CHEM' '59')
# lab_profile.add_aliquot_type(chemistry)

wb = AliquotType(name='Whole Blood', alpha_code='WB', numeric_code='02')
wb.add_derivatives(bc, pl, serum, fbc)

# TODO: Get correct sample codes from LIS
qfc = AliquotType(
    name='Quantitative FC', alpha_code='QFC', numeric_code='61')

# TODO: Get correct sample codes from LIS
csf_store = AliquotType(
    name='CSF STORE', alpha_code='CSF', numeric_code='62')

# TODO: Get correct sample codes from LIS
csf = AliquotType(
    name='Cerebro Spinal Fluid', alpha_code='CSF', numeric_code='56')
csf.add_derivatives(qfc, csf_store)

processing_profile = ProcessingProfile(name='spinal_fluid', aliquot_type=csf)
process_qfc = Process(aliquot_type=qfc, aliquot_count=10)
process_csf_store = Process(aliquot_type=csf_store, aliquot_count=1)
processing_profile.add_processes(process_qfc, process_csf_store)

csf_panel = RequisitionPanel(
    name='Spinal Fluid',
    aliquot_type=csf,
    processing_profile=processing_profile)
lab_profile.add_panel(csf_panel)

viral_load_processing = ProcessingProfile(name='viral_load', aliquot_type=wb)
vl_pl_process = Process(aliquot_type=pl, aliquot_count=3)
vl_bc_process = Process(aliquot_type=bc, aliquot_count=1)
viral_load_processing.add_processes(vl_pl_process, vl_bc_process)

viral_load_panel = RequisitionPanel(
    name='Viral Load',
    aliquot_type=wb,
    processing_profile=viral_load_processing)
lab_profile.add_panel(viral_load_panel)

cd4_processing = ProcessingProfile(name='CD4', aliquot_type=wb)

cd4_panel = RequisitionPanel(
    name='CD4',
    aliquot_type=wb,
    processing_profile=cd4_processing)
lab_profile.add_panel(cd4_panel)

fbc_processing = ProcessingProfile(name='FBC', aliquot_type=wb)

fbc_panel = RequisitionPanel(
    name='Full Blood Count',
    aliquot_type=wb,
    processing_profile=fbc_processing)
lab_profile.add_panel(fbc_panel)

chemistry_alt_processing = ProcessingProfile(
    name='chem + alt', aliquot_type=wb)

chemistry_alt_panel = RequisitionPanel(
    name='Creat, Urea, Elec, ALT',
    aliquot_type=wb,
    processing_profile=chemistry_alt_processing)
lab_profile.add_panel(chemistry_alt_panel)

chemistry_processing = ProcessingProfile(name='chem', aliquot_type=wb)

chemistry_panel = RequisitionPanel(
    name='Creat, Urea, Elec',
    aliquot_type=wb,
    processing_profile=chemistry_processing)
lab_profile.add_panel(chemistry_panel)

site_labs.register(
    lab_profile, requisition_model='ambition_subject.subjectrequisition')
