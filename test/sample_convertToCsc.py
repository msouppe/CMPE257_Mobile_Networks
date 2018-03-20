# Load the jinja library's namespace into the current module.
from jinja2 import Environment, FileSystemLoader
import os
import sys

# In this case, we will load templates off the filesystem.
# This means we must construct a FileSystemLoader object.
# 
# The search path can be used to make finding templates by
#   relative paths much easier.  In this case, we are using
#   absolute paths and thus set it to the filesystem root.
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# An environment provides the data necessary to read and
#   parse our templates.  We pass in the loader object here.
templateEnv = Environment( loader=FileSystemLoader(THIS_DIR),
                         trim_blocks=True )

# This constant string specifies the template file we will use.
TEMPLATE_FILE = "test.csc"

# Read the template file using the environment object.
# This also constructs our Template object.
template = templateEnv.get_template( TEMPLATE_FILE )

# Specify any input variables to the template as a dictionary.
templateVars = { "random_seed" : "12313" }

# Finally, process the template to produce our final text.
outputText = template.render( templateVars )

# Create new file simulation with write privalages
f = open('blah.csc', 'w')

# New file with new variables
f.write(outputText)

