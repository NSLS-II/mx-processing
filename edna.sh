#$/bin/bash
export PROJDIR=/GPFS/CENTRAL/xf17id1/skinnerProjectsBackup
export LSDCHOME=${PROJDIR}/lsdc
export PYTHONPATH=${PROJDIR}/lsdc:$PYTHONPATH
export MONGODB_HOST='xf17id1-lsdcmongo.nsls2.bnl.local'
export BEAMLINE_ID='fmx' # TODO required to keep daq_utils happy
/opt/conda_envs/mx-processing-env/bin/python ${PROJDIR}/mx-processing/edna.py "$@"
