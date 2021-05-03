#$/bin/bash
conda activate lsdcServer_2020-1.0
export PROJDIR=/home/jaishima/code
export PYTHONPATH=${PROJDIR}/lsdc:$PYTHONPATH
export WRAPPERSDIR=$PROJDIR}/wrappers/
python ${PROJDIR}/mx_processing/fast_dp.py "$@"
