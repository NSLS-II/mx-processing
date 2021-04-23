#$/usr/bin/env python3
import os
import os.path
import db_lib
from daq_utils import getBlConfig

collection_id, row_index = sys.argv[0:2]
cbf_comm = getBlConfig('cbf_comm')

request = db_lib.getRequestByID(collection_id)
directory = request["request_obj"]["directory"]
prefix = request["request_obj"]["file_prefix"]
seq_num = 100#request[] #not stored at the moment
row_cell_count = request["request_obj"]["rasterDef"]["rowDefs"][0]["numsteps"]

hdf_sample_data_pattern = os.path.join(directory, f'{prefix}_')
hdf_row_file_pattern = f'{hdf_sample_data_pattern}{int(float(seq_num))}_master.h5'
cbf_conversion_pattern = os.path.join(cbfDir, f'{prefix}_{row_index}_')
cbf_pattern = cbf_conversion_pattern + "*.cbf"

startIndex = (row_index*row_cell_count) + 1
endIndex = startIndex+row_cell_count-1

logger.debug(directory, prefix, row_cell_count, hdf_sample_data_pattern, hdf_row_file_pattern, cbf_conversion_pattern, cbf_pattern, startIndex, endIndex)
os.makedirs(os.path.join(directory, 'cbf'))
command_string = "{cbf_comm} {hdf_row_file_pattern} {startIndex}:{endIndex} {cbf_conversion_pattern}"
os.system(command_string)
