#$/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )" #https://stackoverflow.com/questions/59895/how-can-i-get-the-source-directory-of-a-bash-script-from-within-the-script-itsel
source ${SCRIPT_DIR}/config.sh
${ENV_PATH}/bin/python ${PROCESSINGSCRIPTSDIR}/fast_dp.py "$@"
