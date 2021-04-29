#$/usr/bin/env python3
#run dials spotfinding to process rastering rows
# arguments:
# collection_id - uuid
# row_index - number of row to process

# note, all of the parameters handling has been moved here to prevent this being passed through the ssh command

import os
import sys
import os.path
import db_lib
from daq_utils import getBlConfig
from config_params import * #RASTER_ parameters

collection_id, row_index, seqNum = sys.argv[1:4]
#TODO store beamline and detector so that we don't need to check seqNum
row_index = int(row_index)
if len(sys.argv) > 3:
    active_only = False
else:
    active_only = True

dials_comm = getBlConfig("dialsComm")
dials_tune_low_res = getBlConfig(RASTER_TUNE_LOW_RES)
dials_tune_high_res = getBlConfig(RASTER_TUNE_HIGH_RES)
dials_tune_ice_ring_flag = getBlConfig(RASTER_TUNE_ICE_RING_FLAG)
dials_tune_reso_flag = getBlConfig(RASTER_TUNE_RESO_FLAG)
dials_tune_thresh_flag = getBlConfig("rasterThreshFlag")    
dials_tune_ice_rRng_width = getBlConfig(RASTER_TUNE_ICE_RING_WIDTH)
dials_tune_min_spot_size = getBlConfig("rasterDefaultMinSpotSize")
dials_tune_thresh_kern =  getBlConfig("rasterThreshKernSize")
dials_tune_thresh_sig_bck =  getBlConfig("rasterThreshSigBckrnd")
dials_tune_thresh_sig_strong =  getBlConfig("rasterThreshSigStrong")
dials_comm_with_params = []
if (dials_tuneIceRingFlag):
    dials_comm_with_params.append("ice_rings.filter=true")
    dials_comm_with_params.append(f"ice_rings.width={dials_tuneIceRingWidth}")
if (dials_tuneThreshFlag):
    dials_comm_with_params.append(f"spotfinder.threshold.xds.kernel_size={dials_tuneThreshKern},{dials_tuneThreshKern}")
    dials_comm_with_params.append(f"spotfinder.threshold.xds.sigma_background={dials_tuneThreshSigBck}")
    dials_comm_with_params.append(f"spotfinder.threshold.xds.sigma_strong={dials_tuneThreshSigStrong}")
if (dials_tuneResoFlag):
    dials_comm_with_params.append(f"spotfinder.filter.d_min={dials_tuneHighRes}")
    dials_comm_with_params.append(f"spotfinder.filter.d_max={dials_tuneLowRes}")
if (daq_utils.beamline == "amx"):
    dials_comm_with_params.append(f"min_spot_size={dials_tuneMinSpotSize}")
full_dials_command = ' '.join(dials_comm_with_params)
logger.info('dials spotfinder command: %s' % dials_comm_with_params) 

request = db_lib.getRequestByID(collection_id, active_only)
directory = request["request_obj"]["directory"]
if seqNum>1:
    CBF_pattern = os.path.join(directory, 'cbf', f'{file_prefix}_{seqNum}_*.cbf')
else:
    CBF_pattern = os.path.join(directory, 'cbf', f'prefix_{row_index}_*.cbf')
request = db_lib.getRequestByID(collection_id, active_only)
directory = request["request_obj"]["directory"]

comm_s = f"ls {CBF_pattern} | {full_dials_command}"
os.system(comm_s)
