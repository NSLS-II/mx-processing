export ENV_PATH="/opt/conda_envs/lsdc-processing"
export PROJDIR=/GPFS/CENTRAL/xf17id2/skinnerProjectsBackup/
export LSDCDIR=${PROJDIR}/lsdc
export PROCESSINGDIR=${PROJDIR}/mx-processing
export PYTHONPATH=${LSDCDIR}:$PYTHONPATH
export WRAPPERSDIR=${PROJDIR}/wrappers/
export MONGODB_HOST='xf17id2-lsdcmongo'
export BEAMLINE_ID='fmx' # TODO required to keep daq_utils happy
