#!/usr/bin/env python

# Load the jinja library's namespace into the current module.
from jinja2 import Environment, FileSystemLoader
import javarandom
import os
import sys
import yaml
import random

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
rand = javarandom.Random()

# Init x and y coordinate arrays for Jijna parsing
x_coords = []
y_coords = []
    

for data in yaml.load_all(f):

    # Random coordinate generator w/ Java random seed
    #rand.setSeed(data["randomSeed"])
    
    # Choose fixed values for the x,y coordinates for motes
    for i in range(data["numMotes"]):
        if (data["random"] == False ):    
            x_coords.append(str(1))
            y_coords.append(str(1))
        else:
            x_coords.append(str(rand.nextInt(8000)))
            y_coords.append(str(rand.nextInt(6000)))
    
    # Merges the two arrays of x and y coordinates for easier Jijna parsing
    coordinates = zip(x_coords, y_coords)
    
    # Specify any input variables to the template as a dictionary.
    templateVars = { "RANDOM_SEED" : str(data["randomSeed"]),
                           "MOTES" : data["numMotes"],
                         "COORD" : coordinates                    }
        
    # Process the template to produce our final text.
    outputText = template.render( templateVars )

    # Create new file simulation with write privalages
    f = open('simTest_'+ str(counter) +'.csc', 'w')

    # New file with new variables
    f.write(outputText)

    # Counter used for simulation filename index
    counter += 1