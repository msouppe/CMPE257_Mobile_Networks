#!/bin/bash
# [wf] series of steps required to execute the pipeline.
# This file should contain the series of steps that are required to execute
# the pipeline. Any non-zero exit code will be interpreted as a failure
# by the 'popper check' command.
set -ex

# Run simulation files in simulation folder in contiki.
for file in simulations/*.csc; do
   echo "$file"
   # ant run_nogui -Dargs="$absolutePath/$file" 
   docker run -v `pwd`:/experiment --workdir=/experiment/contiki/tools/cooja --entrypoint=ant terrain run_nogui -Dargs=/experiment"/$file"
   docker cp contiki/tools/cooja/build/COOJA.testlog output/"${file}_log".log
   # cp $logPath $outputPath/"${file}_log".log
done

exit 0
