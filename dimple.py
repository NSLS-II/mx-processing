#$/usr/bin/env python3
import os
import sys
import os.path
import db_lib
from daq_utils import getBlConfig

collection_id, seq_num = sys.argv[1:3]
if len(sys.argv) > 4:
    only_active_proc = False
else:
    only_active_proc = True

result = db_lib.getRequestByID(collection_id, only_active_proc)
beamline = result['beamline']
sample_id = result['sample']
sample = db_lib.getSampleByID(sample_id)
try:
    model_filename = sample["model"]
    if model_filename == 'nan':
        model_pdb_name = "model.pdb"
    else:
        model_pdb_name = f"{model_filename}.pdb"
except KeyError:
    model_pdb_name = "model.pdb"

directory = request["request_obj"]["directory"]
base_directory = request["request_obj"]["basePath"]
dimple_running_dir = os.path.join(directory, 'dimpleOutput')
fastdp_running_dir = os.path.join(directory, 'fastDPOutput')
dimple_comm = f'{getBlConfig("dimpleComm", beamline)}'

os.makedirs(dimple_running_dir)
os.chdir(dimple_running_dir)
mtz_file = os.path.join(fastdp_running_dir, 'fast_dp.mtz')
model_file = os.path.join(base_directory, model_pdb_name)
comm_s = f"{dimple_comm} {running_dir} {mtz_file} {model_file} {dimple_running_dir}"
print(f'Dimple invocation: {comm_s}')
os.system(comm_s)
