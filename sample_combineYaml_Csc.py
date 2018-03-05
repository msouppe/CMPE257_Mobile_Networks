# Load the jinja library's namespace into the current module.
from jinja2 import Environment, FileSystemLoader
import os
import sys
import yaml

# data["randomSeed"]
# data["numMotes"]
# data["x_placement"]
# data["y_placement"]
# data["terrain"]

# Open YAML file with all of the paramters
f = open('simple.yaml', 'r')

# The search path can be used to make finding templates by
#   relative paths much easier.  In this case, we are using
#   absolute paths and thus set it to the filesystem root.
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.
templateEnv = Environment( loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True )

# This constant string specifies the template file we will use.
TEMPLATE_FILE = "template.csc"

# Read the template file using the environment object.
# This also constructs our Template object.
template = templateEnv.get_template( TEMPLATE_FILE )

counter = 0

for data in yaml.load_all(f):

	# Specify any input variables to the template as a dictionary.
    templateVars = { "random_seed" : str(data["randomSeed"]),
                           "motes" : data["numMotes"]}

    # Finally, process the template to produce our final text.
    outputText = template.render( templateVars )

    # Create new file simulation with write privalages
    f = open('blah_'+ str(counter) +'.csc', 'w')

    # New file with new variables
    f.write(outputText)

    counter += 1

