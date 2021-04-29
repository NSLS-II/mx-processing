#$/usr/bin/env python3
#xia2.py - run xia2 to process datasets
# arguments:
# collection_id - uuid

import os
import sys
import os.path
import db_lib
from daq_utils import getBlConfig

collection_id = sys.argv[1:2]
if len(sys.argv) > 1:
    active_only = False
else:
    active_only = True

request = db_lib.getRequestByID(collection_id, active_only)
directory = request["request_obj"]["directory"]
prefix = request["request_obj"]["prefix"]
sweep_start = float(request["request_obj"]["sweep_start"])
sweep_end = float(request["request_obj"]["sweep_end"])
img_width = float(request["request_obj"]["img_width"])
num_images = round(abs(sweep_end - sweep_start) / img_width)
file_number_start = request["request_obj"]["file_number_start"]
comm_s = f"{os.environ['LSDCHOME']}/runXia2.py {directory} {prefix} {file_number_start} {num_images} {collection_id}"
os.system(comm_s)
