import os
import sys
import db_lib
import daq_utils

dna_directory, collection_id, cbf1, cbf2, transmission_percent, flux, xbeam_size, ybeam_size = sys.argv[1:9]
if len(sys.argv)>8:
    active_only = False
else:
    active_only = True

result = db_lib.getRequestByID(collection_id, active_only)
beamline = result['request_obj']['beamline']
os.environ['EDNA_SITE'] = f"NSLS2_{beamline.upper()}"
os.environ['LD_LIBRARY_PATH'] += ':/usr/lib64/raddose-v2-20-05-09'  # TODO verify raddose location in RPM. verify correct method to use this key in python
transmission_percent = float(transmission_percent)
comm_s = f'cd {dna_directory};{os.environ["LSDCHOME"]}/runEdna.py {cbf1} {cbf2} {transmission_percent} {flux} {xbeam_size} {ybeam_size} {collection_id} {beamline}'
print(f'EDNA call: {comm_s}')
os.system(comm_s)
