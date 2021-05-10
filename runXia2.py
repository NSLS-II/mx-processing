#!/usr/bin/python
import time
import os
import os.path
import sys
import db_lib
import json
import daq_utils

def create_filename(prefix,number):
  if (detector_id == "EIGER-16"):
   tmp_filename = findH5FirstData(prefix)
  else:
    tmp_filename = "%s_%05d.cbf" % (prefix,int(number))
  if (prefix[0] != "/"):
    cwd = os.getcwd()
    filename = "%s/%s" % (cwd,tmp_filename)
  else:
    filename = tmp_filename
  return filename

def findH5FirstData(prefix):
  comm_s = "ls " + prefix + "*_data_000001.h5"
  firstDataFilename = os.popen(comm_s).read()[0:-1]
  return firstDataFilename

request_id = sys.argv[1]
request = db_lib.getRequestFromID(request_id)
directory = request["directory"]
runningDir = os.path.join(directory, "xia2Output")
os.makedirs(runningDir, exist_ok=True)
os.chdir(runningDir)

filePrefix = request["prefix"]
numstart = int(request["file_number_start"])
sweep_end = float(request["sweep_end"])
sweep_start = float(request["sweep_start"])
img_width = float(request["img_width"])
numimages = round(abs(sweep_end-sweep_start)/img_width)

expectedFilenameList = []
timeoutLimit = 60 #for now
prefix_long = os.path.join(directory, filePrefix)
for i in range (numstart,numstart+numimages):
  filename = daq_utils.create_filename(prefix_long,i)
  expectedFilenameList.append(filename)
timeout_check = 0
while(not os.path.exists(expectedFilenameList[len(expectedFilenameList)-1])): #this waits for images
  timeout_check = timeout_check + 1
  time.sleep(1.0)
  if (timeout_check > timeoutLimit):
    break
comm_s = "xia2 " + directory
print(comm_s)
os.system(comm_s)
with open("xia2.json") as fd:
    resultObj = json.loads(fd.read())
print(resultObj)
db_lib.addResultforRequest("xia2",request_id,resultObj)
print("finished xia2")
