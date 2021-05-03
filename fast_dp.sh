#$/bin/bash
conda activate lsdcServer_2020-1.0
export PROJDIR=/GPFS/CENTRAL/xf17id1/skinnerProjectsBackup/
export PYTHONPATH=${PROJDIR}/lsdc:$PYTHONPATH
export WRAPPERSDIR=$PROJDIR}/wrappers/
python ${PROJDIR}/mx_processing/fast_dp.py "$@"
