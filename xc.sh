#!/bin/bash
#
# xc
#
# Author: Marcio Pessoa <marcio.pessoa@gmail.com>
# Contributors: none
#
# Description:
#   Start up script file
#
# Example:
#   xc -h
#
# Change log:
# 2019-09-03
#          * Changed: Removed Python 2 support.
#
# 2019-01-01
#          * Changed: Python 3 ready.
#
# 2018-07-18
#          * Fixed: Not returning the xc.pyc exit status.
#          * Fixed: Not undestanding -v option.
#
# 2017-03-05
#          * Fixed: --verbosity option was using an unmutable value (4).
#
# 2017-02-03
#          * First version.
#

#
readonly WORK_DIR='/opt/xc'
readonly WORK_FILE='xc.py'
readonly PYTHON='python3'

# Default values
command="gui"
verbosity=4

# Identify user defined verbosity
declare -a args=($@)
for (( i = 0; i < ${#args[*]}; i++ )); do
  if [ "${args[$i]}" == "--verbosity" ] || [ "${args[$i]}" == "-v" ]; then
    verbosity=${args[$i+1]}
    break
  fi
  if [ "$(echo "${args[$i]}" | cut -d '=' -f 1)" == "--verbosity" ]; then
    verbosity=$(echo "${args[$i]}" | cut -d '=' -f 2)
    break
  fi
done

# Apply desired command
if [ "$#" -eq 0 ]; then
  "$PYTHON" "$WORK_DIR"/"$WORK_FILE" "$command" \
    --verbosity="$verbosity"
  exit ${PIPESTATUS[0]}
else
  "$PYTHON" "$WORK_DIR"/"$WORK_FILE" "$@" \
    --verbosity="$verbosity"
  exit ${PIPESTATUS[0]}
fi
