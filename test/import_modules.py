#!/usr/bin/env python

import os
import sys

# Check if pip is installed on current OS
def pip():
	try:
		import pip
	except ImportError, e:
		os_sys = system.platform

		# Linux (2.x and 3.x)
		if os_sys == 'linux2':
			os.system('apt-get install python-pip python-dev build-essential')

		# Windows
		elif os_sys == 'win32':
			os.system('')

		# Windows/Cygwin
		elif os_sys == 'cygwin':
			os.system('')

		# Mac OS X
		elif os_sys == 'darwin':
			os.system('easy_install pip')

		# OS/2
		elif os_sys == 'os2':
			os.system('')

		# OS/2 EMX
		elif os_sys == 'os2emx':
			os.system('')

		# RiscOS
		elif os_sys == 'riscos':
			os.system('')

		#AtheOS
		elif os_sys == 'atheos':
			os.system('')

		# Unavailable OS
		else:
			print('Error: Unable to install pip for system')


# Check if jinja2 is installed
def jijna():
	try:
		import jinja2
	except ImportError, e:
		os.system('pip install Jinja2')

# Check if pyyaml is installed
def pyyaml():
	try:
		import pyyaml
	except ImportError, e:
		os.system('pip install pyyaml')

# Check if java-random is installed
def random():
	try:
		import javarandom
	except ImportError, e:
		os.system('pip install java-random')

def main():
	pip()
	jijna()
	pyyaml()
	random()

if __name__ == "__main__":
	main()
