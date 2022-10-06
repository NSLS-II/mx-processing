#run dials spotfinding to process rastering rows
# arguments:
# collection_id - uuid
# row_index - number of row to process
# seqNum    - sequence number of collection
# per_image - ignore row_index, process all without specifying the row_index or 'Raster' in name - no particular value required
#             meant to be used for per-image analysis, which coarsely samples images to convert

# note, all of the parameters handling has been moved here to prevent this being passed through the ssh command

import os
import sys
import os.path
import db_lib
from daq_utils import getBlConfig
from config_params import * #RASTER_ parameters

try:
    collection_id, row_index, seqNum, per_image = sys.argv[1:5]
    per_image = True
except ValueError:
    collection_id, row_index, seqNum = sys.argv[1:4]
    per_image = False
#TODO store beamline and detector so that we don't need to check seqNum
seqNum = int(seqNum)
row_index = int(row_index)
if len(sys.argv) > 5:
    active_only = False
else:
    active_only = True

request = db_lib.getRequestByID(collection_id, active_only)
beamline = request['request_obj']['beamline']

dials_comm = getBlConfig("dialsComm", beamline)
dials_tune_low_res = getBlConfig(RASTER_TUNE_LOW_RES, beamline)
dials_tune_high_res = getBlConfig(RASTER_TUNE_HIGH_RES, beamline)
dials_tune_ice_ring_flag = getBlConfig(RASTER_TUNE_ICE_RING_FLAG, beamline)
dials_tune_reso_flag = getBlConfig(RASTER_TUNE_RESO_FLAG, beamline)
dials_tune_thresh_flag = getBlConfig("rasterThreshFlag", beamline)    
dials_tune_ice_ring_width = getBlConfig(RASTER_TUNE_ICE_RING_WIDTH, beamline)
dials_tune_min_spot_size = getBlConfig("rasterDefaultMinSpotSize", beamline)
dials_tune_thresh_kern =  getBlConfig("rasterThreshKernSize", beamline)
dials_tune_thresh_sig_bck =  getBlConfig("rasterThreshSigBckrnd", beamline)
dials_tune_thresh_sig_strong =  getBlConfig("rasterThreshSigStrong", beamline)
dials_comm_with_params = []
if (dials_tune_ice_ring_flag):
    dials_comm_with_params.append("ice_rings.filter=true")
    dials_comm_with_params.append(f"ice_rings.width={dials_tune_ice_ring_width}")
if (dials_tune_thresh_flag):
    dials_comm_with_params.append(f"spotfinder.threshold.xds.kernel_size={dials_tune_thresh_kern},{dials_tune_thresh_kern}")
    dials_comm_with_params.append(f"spotfinder.threshold.xds.sigma_background={dials_tune_thresh_sig_bck}")
    dials_comm_with_params.append(f"spotfinder.threshold.xds.sigma_strong={dials_tune_thresh_sig_strong}")
if (dials_tune_reso_flag):
    dials_comm_with_params.append(f"spotfinder.filter.d_min={dials_tune_high_res}")
    dials_comm_with_params.append(f"spotfinder.filter.d_max={dials_tune_low_res}")
if beamline == "amx":
    dials_comm_with_params.append(f"min_spot_size={dials_tune_min_spot_size}")
full_dials_command = f'{dials_comm} {" ".join(dials_comm_with_params)}'
print('dials spotfinder command: %s' % dials_comm_with_params) 

directory = request["request_obj"]["directory"]
file_prefix = request["request_obj"]["file_prefix"]
if per_image:
    CBF_pattern = os.path.join(directory, 'cbf', f'{file_prefix}*.cbf')
elif seqNum>1:
    CBF_pattern = os.path.join(directory, 'cbf', f'{file_prefix}_Raster_{row_index}_*.cbf')
else:
    CBF_pattern = os.path.join(directory, 'cbf', f'prefix_{row_index}_*.cbf')

comm_s = f"ls {CBF_pattern} | {full_dials_command}"
os.system(comm_s)
