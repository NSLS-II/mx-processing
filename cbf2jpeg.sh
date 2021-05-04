#$/bin/bash
export PROJDIR=/GPFS/CENTRAL/xf17id1/skinnerProjectsBackup/
export PYTHONPATH=${PROJDIR}/lsdc:$PYTHONPATH
export WRAPPERSDIR=${PROJDIR}/wrappers/
export BEAMLINE_ID='fmx' # TODO required to keep daq_utils happy
/opt/conda_envs/mx-processing-env/bin/python ${PROJDIR}/mx-processing/cbf2jpeg.py "$@"
