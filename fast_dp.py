import os
import sys
import os.path
import db_lib
from daq_utils import getBlConfig

collection_id, seq_num = sys.argv[1:3]
if len(sys.argv) > 2:
    only_active_proc = False
else:
    only_active_proc = True

result = db_lib.getRequestByID(collection_id, only_active_proc)
beamline = result["request_obj"]['beamline']
directory = result["request_obj"]["directory"]
running_dir = os.path.join(directory, 'fastDPOutput')
file_prefix = result["request_obj"]["file_prefix"]
prefix_long = os.path.join(directory, f'{file_prefix}_{seq_num}')
hdf_file_pattern = f'{prefix_long}_master.h5'
fast_dp_comm = f'source {os.environ["WRAPPERSDIR"]}/fastDPWrap2;{getBlConfig("fastdpComm", beamline)}'
comm_s = f"cd {running_dir};{fast_dp_comm} {hdf_file_pattern}"
print(f'Fast DP invocation: {comm_s}')
os.system(comm_s)
