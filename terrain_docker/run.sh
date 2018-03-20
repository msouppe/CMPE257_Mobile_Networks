#!/bin/bash
# [wf] series of steps required to execute the pipeline.
# This file should contain the series of steps that are required to execute
# the pipeline. Any non-zero exit code will be interpreted as a failure
# by the 'popper check' command.
set -e

# 
cd simulations/

# Get 
absolutePath=$(pwd)

# Go into Cooja folder to run simulations.
cd ../contiki/tools/cooja

outputPath=../../../output
logPath=build/COOJA.testlog

#JAVA_HOME=/usr ; export JAVA_HOME

# Get each file in the simulation directory and save to variable.
filenames=$(ls ../../../simulations/)

# Run simulation files in simulation folder in contiki.
for file in $filenames; do
   # echo "$file"
   # ant run_nogui -Dargs="$absolutePath/$file" 
   docker run -v `pwd`:/experiment --workdir=/experiment/contiki/tools/cooja terrain ant run_nogui -Dargs="$absolutePath/$file"
   docker cp :/experiment/contiki/tools/cooja/build/COOJA.testlog $outputPath/"${file}_log".log
   # cp $logPath $outputPath/"${file}_log".log
done

exit 0
