#$/usr/bin/env python3
#eiger2cbf currently designed for rastering rows. could be more general
# arguments:
# collection_id - uuid
# start_index - first image of hdf5 file to convert
# end_index - last image of hdf5 file to convert
# sweep_start - set to 0 if not part of a row
# seq_num - collection sequence number

import os
import sys
import os.path
import db_lib
from daq_utils import getBlConfig

collection_id, start_index, end_index, sweep_start, seq_num = sys.argv[1:6]
start_index = int(start_index)
end_index = int(end_index)
sweep_start = int(sweep_start)
seq_num = int(seq_num)
if len(sys.argv) > 6:
    active_only = False
else:
    active_only = True

request = db_lib.getRequestByID(collection_id, active_only)
beamline = request['beamline']
directory = request["request_obj"]["directory"]
if request["request_obj"]["protocol"] == "raster":
    prefix = f'{request["request_obj"]["file_prefix"]}_Raster'
elif request["request_obj"]["protocol"] in ("ednaCol", "characterize")
    prefix = f'ref-{request["request_obj"]["file_prefix"]}'
else:
    prefix = request["request_obj"]["file_prefix"]
row_cell_count = request["request_obj"]["rasterDef"]["rowDefs"][0]["numsteps"]

hdf_sample_data_pattern = os.path.join(directory, f'{prefix}_')
hdf_row_file_pattern = f'{hdf_sample_data_pattern}{int(float(seq_num))}_master.h5'
cbf_dir = os.path.join(directory, 'cbf')
if sweep_start > 0:
    cbf_conversion_pattern = os.path.join(cbf_dir, f'{prefix}_{sweep_start}_')
else:
    cbf_conversion_pattern = os.path.join(cbf_dir, f'{prefix}_')
cbf_pattern = cbf_conversion_pattern + "*.cbf"

os.makedirs(cbf_dir)
cbf_comm = getBlConfig('cbfComm', beamline)
comm_s = f"{cbf_comm} {hdf_row_file_pattern} {start_index}:{end_index} {cbf_conversion_pattern}"
os.system(comm_s)
