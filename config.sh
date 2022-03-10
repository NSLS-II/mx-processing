export ENV_PATH="/opt/conda_envs/lsdc-processing-2022-1.0"
export PROJDIR=/GPFS/CENTRAL/xf17id2/skinnerProjectsBackup/
export LSDCDIR=${PROJDIR}/lsdc
export PROCESSINGDIR=${PROJDIR}/lsdc-processing
export PYTHONPATH=${LSDCDIR}:$PYTHONPATH
export WRAPPERSDIR=${PROJDIR}/wrappers/
export MONGODB_HOST='xf17id2-lsdcmongo'
export BEAMLINE_ID='fmx' # TODO required to keep daq_utils happy
