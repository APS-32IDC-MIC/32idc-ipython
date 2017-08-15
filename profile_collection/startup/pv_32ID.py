# -*- coding: utf-8 -*-
# """
# Transmission X-ray Microscope process variables grouped by component
# 
# """
# 
from ophyd import (EpicsMotor, Device, Component, EpicsSignal,
                   EpicsSignalRO)
 
# User Status
user_name = EpicsMotor('32idcTXM:UserName', name='user_name')
user_affiliation = EpicsMotor('32idcTXM:UserInstitution', name='user_affiliation')
user_badge = EpicsMotor('32idcTXM:UserBadge', name='user_badge')
user_email = EpicsMotor('32idcTXM:UserEmail', name='user_email')
proposal_number = EpicsMotor('32idcTXM:ProposalNumber', name='')
proposal_title = EpicsMotor('32idcTXM:ProposalTitle', name='proposal_number')
user_info_update_time = EpicsMotor('32idcTXM:UserInfoUpdate', name='user_info_update_time')
file_name = EpicsMotor('32idcPG3:HDF1:FileName', name='file_name')
file_path = EpicsMotor('32idcPG3:HDF1:FilePath_RBV', name='file_path')
 
# beamline Status
date_time = EpicsMotor('S:IOC:timeOfDayISO8601', name='date_time')
current = EpicsMotor('S:SRcurrentAI', name='current')
top_up_status = EpicsMotor('S:TopUpStatus', name='top_up_status')
source_energy = EpicsMotor('ID32ds:Energy.VAL', name='source_energy')
source_gap = EpicsMotor('ID32ds:Gap.VAL', name='source_gap')
energy_dcm = EpicsMotor('32ida:BraggEAO.VAL', name='energy_dcm')
mirror_x  = EpicsMotor('32idbMIR:m1.RBV', name='mirror_x')
mirror_y  = EpicsMotor('32idbMIR:m2.RBV', name='mirror_y')
 
# Table microCT
table_x_upstream = EpicsMotor('32idc02:m1.VAL', name='table_x_upstream')
table_y_upstream = EpicsMotor('32idc02:m2.VAL', name='table_y_upstream')
table_x_downstream = EpicsMotor('32idc02:m4.VAL', name='table_x_downstream')
table_y_downstream = EpicsMotor('32idc02:m3.VAL', name='table_y_downstream')
table_x_upstream_dial = EpicsMotor('32idc02:m1.DVAL', name='table_x_upstream_dial')
table_y_upstream_dial = EpicsMotor('32idc02:m2.DVAL', name='table_y_upstream_dial')
table_x_downstream_dial = EpicsMotor('32idc02:m4.DVAL', name='table_x_downstream_dial')
table_y_downstream_dial = EpicsMotor('32idc02:m3.DVAL', name='table_y_downstream_dial')

# Sample microCT
sample_x_mct = EpicsMotor('32idc02:m31.VAL', name='sample_x_mct')
sample_y_mct = EpicsMotor('32idc02:m25.VAL', name='sample_y_mct')
sample_top_x_mct = EpicsMotor('32idc01:m104.VAL', name='sample_top_x_mct')
sample_top_z_mct = EpicsMotor('32idc01:m105.VAL', name='sample_top_z_mct')
sample_rotary_mct = EpicsMotor('32idc02:m11.VAL', name='sample_rotary_mct')
sample_yaw_mct = EpicsMotor('32idc02:m30.VAL', name='sample_yaw_mct')
sample_pitch_mct = EpicsMotor('32idc02:m29.VAL', name='sample_pitch_mct')

sample_x_mct_dial = EpicsMotor('32idc02:m31.DVAL', name='sample_x_mct_dial')
sample_y_mct_dial = EpicsMotor('32idc02:m25.DVAL', name='sample_y_mct_dial')
sample_top_x_mct_dial = EpicsMotor('32idc01:m104.DVAL', name='sample_top_x_mct_dial')
sample_top_z_mct_dial = EpicsMotor('32idc01:m105.DVAL', name='sample_top_z_mct_dial')
sample_rotary_mct_dial = EpicsMotor('32idc02:m11.DVAL', name='sample_rotary_mct_dial')
sample_yaw_mct_dial = EpicsMotor('32idc02:m30.DVAL', name='sample_yaw_mct_dial')
sample_pitch_mct_dial = EpicsMotor('32idc02:m29.DVAL', name='sample_pitch_mct_dial')

# CCD camera microCT
ccd_camera_z_mct = EpicsMotor('32idc02:m20.VAL', name='ccd_camera_z_mct')
ccd_camera_z_mct_dial = EpicsMotor('32idc02:m20.DVAL', name='ccd_camera_z_mct_dial')
ccd_selector_mct = EpicsMotor('32idc02:m21.VAL', name='ccd_selector_mct')
ccd_selector_mct_dial = EpicsMotor('32idc02:m21.DVAL', name='ccd_selector_mct_dial')
ccd_focus_mct = EpicsMotor('32idc02:m22.VAL', name='ccd_focus_mct')
ccd_focus_mct_dial = EpicsMotor('32idc02:m22.DVAL', name='ccd_focus_mct_dial')

scintillator_x_mct = EpicsMotor('32idc01:m101.VAL', name='scintillator_x_mct')
scintillator_y_mct = EpicsMotor('32idc01:m102.VAL', name='scintillator_y_mct')
scintillator_x_mct_dial = EpicsMotor('32idc01:m101.DAL', name='scintillator_x_mct_dial')
scintillator_y_mct_dial = EpicsMotor('32idc01:m102.DVAL', name='scintillator_y_mct_dial')

# TXM
# beam Monitor
beam_monitor_x = EpicsMotor('32idcTXM:xps:c1:m2.VAL', name='beam_monitor_x')
beam_monitor_y = EpicsMotor('32idcTXM:nf:c0:m3.VAL', name='beam_monitor_y')
beam_monitor_x_dial = EpicsMotor('32idcTXM:xps:c1:m2.DVAL', name='beam_monitor_x_dial')
beam_monitor_y_dial = EpicsMotor('32idcTXM:nf:c0:m3.DVAL', name='beam_monitor_y_dial')
 
# Filter
filter_x = EpicsMotor('32idcTXM:xps:c2:m1.VAL', name='filter_x')
filter_x_dial = EpicsMotor('32idcTXM:xps:c2:m1.DVAL', name='filter_x_dial')
 
# Diffuser
diffuser = EpicsMotor('32idcTXM:xps:c1:m6.VAL', name='diffuser')
diffuser_dial = EpicsMotor('32idcTXM:xps:c1:m6.DVAL', name='diffuser_dial')
 
# beam Stop
beam_stop_x = EpicsMotor('32idcTXM:xps:c1:m1.VAL', name='beam_stop_x')
beam_stop_y = EpicsMotor('32idcTXM:nf:c0:m2.VAL', name='beam_stop_y')
beam_stop_x_dial = EpicsMotor('32idcTXM:xps:c1:m1.DVAL', name='beam_stop_x_dial')
beam_stop_y_dial = EpicsMotor('32idcTXM:nf:c0:m2.DVAL', name='beam_stop_y_dial')
 
# CRL
crl_x = EpicsMotor('32idb:m32.VAL', name='crl_x')
crl_y = EpicsMotor('32idb:m28.VAL', name='crl_y')
crl_pitch = EpicsMotor('32idb:m26.VAL', name='crl_pitch')
crl_yaw = EpicsMotor('32idb:m27.VAL', name='crl_yaw')
crl_x_dial = EpicsMotor('32idb:m32.DVAL', name='crl_x_dial')
crl_y_dial = EpicsMotor('32idb:m28.DVAL', name='crl_y_dial')
crl_pitch_dial = EpicsMotor('32idb:m26.DVAL', name='crl_pitch_dial')
crl_yaw_dial = EpicsMotor('32idb:m27.DVAL', name='crl_yaw_dial')
 
# Condenser
condenser_x = EpicsMotor('32idcTXM:xps:c2:m8.VAL', name='condenser_x')
condenser_y = EpicsMotor('32idcTXM:mxv:c1:m2.VAL', name='condenser_y')
condenser_z = EpicsMotor('32idcTXM:mxv:c1:m5.VAL', name='condenser_z')
condenser_x_dial = EpicsMotor('32idcTXM:xps:c2:m8.DVAL', name='condenser_x_dial')
condenser_y_dial = EpicsMotor('32idcTXM:mxv:c1:m2.DVAL', name='condenser_y_dial')
condenser_z_dial = EpicsMotor('32idcTXM:mxv:c1:m5.DVAL', name='condenser_z_dial')
 
# Pin Hole
pin_hole_x = EpicsMotor('32idcTXM:xps:c1:m3.VAL', name='pin_hole_x')
pin_hole_y = EpicsMotor('32idcTXM:xps:c1:m4.VAL', name='pin_hole_y')
pin_hole_z = EpicsMotor('32idcTXM:xps:c1:m5.VAL', name='pin_hole_z')
pin_hole_x_dial = EpicsMotor('32idcTXM:xps:c1:m3.DVAL', name='pin_hole_x_dial')
pin_hole_y_dial = EpicsMotor('32idcTXM:xps:c1:m4.DVAL', name='pin_hole_y_dial')
pin_hole_z_dial = EpicsMotor('32idcTXM:xps:c1:m5.DVAL', name='pin_hole_z_dial')
 
# Sample
sample_x = EpicsMotor('32idcTXM:xps:c1:m8.VAL', name='sample_x')
sample_y = EpicsMotor('32idcTXM:mxv:c1:m1.VAL', name='sample_y')
sample_rotary = EpicsMotor('32idcTXM:hydra:c0:m1', name='sample_rotary')
sample_x_dial = EpicsMotor('32idcTXM:xps:c1:m8.DVAL', name='sample_x_dial')
sample_y_dial = EpicsMotor('32idcTXM:mxv:c1:m1.DVAL', name='sample_y_dial')
sample_rotary_dial = EpicsMotor('32idcTXM:hydra:c0:m1.DVAL', name='sample_rotary_dial')
 
sample_top_x = EpicsMotor('32idcTXM:mcs:c1:m2.VAL', name='sample_top_x')
sample_top_z = EpicsMotor('32idcTXM:mcs:c1:m1.VAL', name='sample_top_z')
sample_top_x_dial = EpicsMotor('32idcTXM:mcs:c1:m2.DVAL', name='sample_top_x_dial')
sample_top_z_dial = EpicsMotor('32idcTXM:mcs:c1:m1.DVAL', name='sample_top_z_dial')
 
# Zone Plate
zone_plate_x = EpicsMotor('32idcTXM:mcs:c2:m2.VAL', name='zone_plate_x')
zone_plate_y = EpicsMotor('32idc01:m110.VAL', name='zone_plate_y')
zone_plate_z = EpicsMotor('32idcTXM:mcs:c2:m3.VAL', name='zone_plate_z')
zone_plate_x_dial = EpicsMotor('32idcTXM:mcs:c2:m2.DVAL', name='zone_plate_x_dial')
zone_plate_y_dial = EpicsMotor('32idc01:m110.DVAL', name='zone_plate_y_dial')
zone_plate_z_dial = EpicsMotor('32idcTXM:mcs:c2:m3.DVAL', name='zone_plate_z_dial')
 
# 2nd Zone Plate
zone_plate_2nd_x = EpicsMotor('32idcTXM:mcs:c0:m3.VAL', name='zone_plate_2nd_x')
zone_plate_2nd_y = EpicsMotor('32idcTXM:mcs:c0:m1.VAL', name='zone_plate_2nd_y')
zone_plate_2nd_z = EpicsMotor('32idcTXM:mcs:c0:m2.VAL', name='zone_plate_2nd_z')
zone_plate_2nd_x_dial = EpicsMotor('32idcTXM:mcs:c0:m3.DVAL', name='zone_plate_2nd_x_dial')
zone_plate_2nd_y_dial = EpicsMotor('32idcTXM:mcs:c0:m1.DVAL', name='zone_plate_2nd_y_dial')
zone_plate_2nd_z_dial = EpicsMotor('32idcTXM:mcs:c0:m2.DVAL', name='zone_plate_2nd_z_dial')
 
# bertrand Lens
bertrand_x = EpicsMotor('32idcTXM:nf:c0:m4.VAL', name='bertrand_x')
bertrand_y = EpicsMotor('32idcTXM:nf:c0:m5.VAL', name='bertrand_y')
bertrand_x_dial = EpicsMotor('32idcTXM:nf:c0:m4.DVAL', name='bertrand_x_dial')
bertrand_y_dial = EpicsMotor('32idcTXM:nf:c0:m5.DVAL', name='bertrand_y_dial')
# 
# Flight Tube
flight_tube_z = EpicsMotor('32idcTXM:mxv:c1:m8.VAL', name='flight_tube_z')
flight_tube_z_dial = EpicsMotor('32idcTXM:mxv:c1:m8.DVAL', name='flight_tube_z_dial')
 
# CCD camera
ccd_camera_x = EpicsMotor('32idcTXM:mxv:c1:m3.VAL', name='ccd_camera_x')
ccd_camera_y = EpicsMotor('32idcTXM:mxv:c1:m4.VAL', name='ccd_camera_y')
ccd_camera_z = EpicsMotor('32idcTXM:mxv:c1:m6.VAL', name='ccd_camera_z')
ccd_camera_x_dial = EpicsMotor('32idcTXM:mxv:c1:m3.DVAL', name='ccd_camera_x_dial')
ccd_camera_y_dial = EpicsMotor('32idcTXM:mxv:c1:m4.DVAL', name='ccd_camera_y_dial')
ccd_camera_z_dial = EpicsMotor('32idcTXM:mxv:c1:m6.DVAL', name='ccd_camera_z_dial')
 

#class CCD(Device):
#    ccd_yaw = Component(EpicsSignal, 'cs:m7, name='')
#    ccd_objective = Component(EpicsSignal, 'cs:m2, name='')

# ccd = CCD('32idcTXM:xps:', name='ccd')

ccd_yaw = EpicsMotor('32idcTXM:xps:c2:m7', name='ccd_yaw')
ccd_objective = EpicsMotor('32idcTXM:xps:c2:m2.VAL', name='ccd_objective')
ccd_yaw_dial = EpicsMotor('32idcTXM:xps:c2:m7.DVAL', name='ccd_yaw_dial')
ccd_objective_dial = EpicsMotor('32idcTXM:xps:c2:m2.DVAL', name='ccd_objective_dial')
 
