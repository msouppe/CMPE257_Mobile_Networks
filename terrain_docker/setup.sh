#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# Create simulations folder if it doesn't exist for simulations.
mkdir -p simulations/

# Create scripts folder if it doesn't exist for python scripts.
mkdir -p scripts/

# Create scripts folder if it doesn't exist for output log.
mkdir -p output/

# Build docker image with dependencies
docker build -t terrain docker/

# Create simulation files
docker run -v `pwd`:/experiment --workdir=/experiment terrain scripts/create_sim_files.py

exit 0
