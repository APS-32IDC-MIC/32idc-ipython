print(__file__)

# EPICS area detector(s)

from ophyd import SingleTrigger, AreaDetector, SimDetector
from ophyd import HDF5Plugin
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd import Component, Device, EpicsSignalWithRBV
from ophyd.areadetector import ADComponent


class MyHDF5Plugin(HDF5Plugin, FileStoreHDF5IterativeWrite):
	
	file_number_sync = None
	array_callbacks = Component(EpicsSignalWithRBV, "ArrayCallbacks")
	enable_callbacks = Component(EpicsSignalWithRBV, "EnableCallbacks")
	
	def get_frames_per_point(self):
		return self.parent.cam.num_images.get()

###
# see: https://github.com/NSLS-II/ophyd/blob/master/ophyd/areadetector/filestore_mixins.py
###	
EPICS_AD_FILE_PATH_TEMPLATE = "/tmp"
DATABROKER_FILE_PATH_ROOT = "/"
###
assert(EPICS_AD_FILE_PATH_TEMPLATE.startswith(DATABROKER_FILE_PATH_ROOT))


 
class MySimDetector(SingleTrigger, SimDetector):

   hdf1 = Component(
           MyHDF5Plugin,
           "HDF1:",
           root=DATABROKER_FILE_PATH_ROOT,
           write_path_template=EPICS_AD_FILE_PATH_TEMPLATE,
           fs=fs,
           )


simdet = MySimDetector('32idcSIM:', name='simdet')
simdet.read_attrs = ['hdf1', 'cam']
simdet.hdf1.read_attrs = ['full_file_name']  # 'image' gets added dynamically
simdet.cam.array_callbacks.put(1)
