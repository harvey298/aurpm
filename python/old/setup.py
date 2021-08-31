print("This is a temp installer!")
bashreco = """
alias aurpm="python $HOME/.aurpm/index.py"
"""
import os
from subprocess import run, PIPE, STDOUT, Popen
import sys
if os.getuid() == 0:
    print("Oh No! I've been given super powers! Do Not run any AURPM component as root!")
    sys.exit(1)
homedir = os.environ['HOME']
print("Changing working directory to " + homedir)
os.chdir(homedir)
if os.path.isdir('.aurpm') == 'True':
    print("Install Path Exists!")
else:
    print("Install Path Doesn't Exists!")
    try:
        os.mkdir(".aurpm")
    except:
        print("I was wrong! the install path Exists! ooops!")
print("Starting main install!")
work = homedir + '/.aurpm'
os.system("git clone https://github.com/harvey298/aurpm.git " + work)
print("AURPM core ready!")
print("we recommend you adding this line into your .bashrc")
print(bashreco)