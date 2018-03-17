import os
import subprocess
from subprocess import call
process = os.popen('pip3 list --outdated')
output = process.readlines()
for k in output:
	m,n = k.split(' ',1)
	call("sudo pip install --upgrade " + m,shell = True)
