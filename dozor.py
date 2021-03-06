#$/usr/bin/env python3
#dozor.py - run dozor to process rastering rows
# arguments:
# collection_id - uuid
# row_index - number of row to process

import os
import sys
import os.path
import db_lib

collection_id, row_index = sys.argv[1:3]
row_index = int(row_index)
if len(sys.argv) > 2:
    active_only = False
else:
    active_only = True

request = db_lib.getRequestByID(collection_id, active_only)
directory = request["request_obj"]["directory"]
dozor_dir = os.path.join(directory, 'dozor', f'row_{row_index}')
dozor_comm = "dozor"
comm_s = f"cd {dozor_dir}; {dozor_comm} -w -bin 1 h5_row_{row_index}.dat"
print(f'dozor call: {comm_s}')
os.system(comm_s)
