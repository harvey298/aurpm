import os,sys,time,json,configparser
from arg import handle
from index import index

from util import permission_check

#pkg = "null"

#homedir = index.home
#whereami = homedir + "/.aurpm"
#whereshouldpackagebe = 'null'
#whereispackage = 'null'
#giturl = 'null'
#os.chdir(whereami)
#print('my work dir ' + whereami)
#workdir = whereami + '/work/'

if __name__ == "__main__":
    permission_check()
    handle()