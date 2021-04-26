#$/usr/bin/env python3
#convert a diffraction image in cbf format to a jpeg, then shrink it - for ISPyB
import os
import os.path
import sys
import db_lib
import daq_utils
from daq_utils import getBlConfig

collection_id = sys.argv[0:1]

result = db_lib.getRequestByID(collection_id)
result_obj = result['result_obj']
request_obj = result_obj['requestObj']
directory = request_obj["directory"]
file_prefix = request_obj['file_prefix']
base_path = request_obj["base_path"]
visit_name = daq_utils.getVisitName()
jpeg_directory = os.path.join(visit_name, "jpegs", directory[directory.find(visit_name)+len(visit_name):len(directory)])
full_jpeg_directory = os.path.join(base_path, jpeg_directory)

cbf_dir = directory
CBF_conversion_pattern = os.path.join(cbf_dir, f'{file_prefix}_')
JPEG_conversion_pattern = os.path.join(full_jpeg_directory, f'{file_prefix}_')

adxv_comm = os.environ["PROJDIR"] + getBlConfig('adxvComm')
comm_s = f'{adxv_comm} -sa {CBF_conversion_pattern}000001.cbf {JPEG_conversion_pattern}0001.jpg'
os.system(comm_s)
comm_s = f'convert {JPEG_conversion_pattern}0001.jpeg -resize 10% {JPEG_conversion_pattern}0001.thumb.jpeg'
os.system(comm_s)
