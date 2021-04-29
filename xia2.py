#$/usr/bin/env python3
#xia2.py - run xia2 to process datasets
# arguments:
# collection_id - uuid

import os
import sys

collection_id = sys.argv[1:2]
comm_s = f"runXia2.py {collection_id}"
os.system(comm_s)
