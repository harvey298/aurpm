print("This is a temp updater!")
import os
from subprocess import run, PIPE, STDOUT, Popen
import sys
if os.getuid() == 0:
    print("Oh No! I've been given super powers! Do Not run any AURPM component as root!")
    sys.exit(1)
homedir = os.environ['HOME']
install = homedir + '/.aurpm'
print("Changing working directory to " + install)
os.chdir(install)
print("updating AURPM now!")
os.system("git pull")
