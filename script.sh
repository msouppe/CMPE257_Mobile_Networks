#!/usr/bin/env python

# Load the jinja library's namespace into the current module.
from jinja2 import Environment, FileSystemLoader
import javarandom
import os
import sys
import yaml

# data["random"]
# data["randomSeed"]
# data["numMotes"]
# data["x_coord"]
# data["y_coord"]
# data["terrain"]

# Open YAML file with all of the paramters
f = open('sim_config.yaml', 'r')

# The search path can be used to make finding templates by
#   relative paths much easier.  In this case, we are using
#   absolute paths and thus set it to the filesystem root.
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.
templateEnv = Environment( loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True )

# This constant string specifies the template file we will use.
TEMPLATE_FILE = "sim_template.csc"

# Read the template file using the environment object.
# This also constructs our Template object.
template = templateEnv.get_template( TEMPLATE_FILE )

# Temp variable to keep track of output files
counter = 0

# Declare java random generator
r = javarandom.Random()

for data in yaml.load_all(f):
    
    # Random coordinate generator w/ Java random seed
    r.setSeed(data["randomSeed"])
    
    # Choose fixed values for the x,y coordinates for motes
    if (data["random"] == False ):
        templateVars = { "RANDOM_SEED" : str(data["randomSeed"]),
                           "MOTES" : data["numMotes"],
                         "X_COORD" : data["x_coord"],
                         "Y_COORD" : data["y_coord"]    }
    
    # Else use random generator to choose x,y mote coordinates
	# Specify any input variables to the template as a dictionary.
    templateVars = { "RANDOM_SEED" : str(data["randomSeed"]),
                           "MOTES" : data["numMotes"],
                         "X_COORD" : r.nextInt(8000),
                         "Y_COORD" : r.nextInt(6000)    }

    # Process the template to produce our final text.
    outputText = template.render( templateVars )

    # Create new file simulation with write privalages
    f = open('simTest_'+ str(counter) +'.csc', 'w')

    # New file with new variables
    f.write(outputText)

    # Counter used for simulation filename index
    counter += 1

