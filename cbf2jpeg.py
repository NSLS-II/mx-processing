#convert a diffraction image in cbf format to a jpeg, then shrink it - for ISPyB
#input parameters - collection_id (uuid) and optional active_only flag - if set, will also search non-active collections

import os
import os.path
import sys
import db_lib
from daq_utils import getBlConfig

collection_id = sys.argv[1]
if len(sys.argv) > 2:
    active_only = False
else:
    active_only = True

result = db_lib.getRequestByID(collection_id, active_only)
beamline = result["request_obj"]['beamline']
request_obj = result['request_obj']
directory = request_obj["directory"]
file_prefix = request_obj['file_prefix']
base_path = request_obj["basePath"]
visit_name = request_obj["visit_name"]
jpeg_directory = os.path.join(visit_name, "jpegs", directory[directory.find(visit_name)+len(visit_name)+1:len(directory)])
full_jpeg_directory = os.path.join(base_path, jpeg_directory)

cbf_dir = directory
CBF_conversion_pattern = os.path.join(cbf_dir, f'{file_prefix}_')
JPEG_conversion_pattern = os.path.join(full_jpeg_directory, f'{file_prefix}_')

adxv_comm = os.path.join(os.environ["PROJDIR"], getBlConfig('adxvComm', beamline))
comm_s = f'{adxv_comm} -sa {CBF_conversion_pattern}000001.cbf {JPEG_conversion_pattern}0001.jpg'
os.system(comm_s)
comm_s = f'convert {JPEG_conversion_pattern}0001.jpeg -resize 10% {JPEG_conversion_pattern}0001.thumb.jpeg'
os.system(comm_s)
