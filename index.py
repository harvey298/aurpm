#!/usr/bin/python3

#--------------------------------------------------------------------------#
#                               Made by Harvey298                          #
#                          Simple AUR Helper | 25 Jan 2021                 #
#                                                                          #
#--------------------------------------------------------------------------#

# Main imports
import os
import sys
from sys import argv
from subprocess import run, PIPE, STDOUT, Popen
import time

# Import urllib
import urllib.request, urllib.error
from urllib.request import urlopen
from urllib.error import URLError

# Other imports
import json
import configparser
import fnmatch

config = configparser.ConfigParser()


# I'm not 100% sure on how classes work so any vars that change I am not putting into a class
class aurinfo:
    url: str = "https://aur.archlinux.org"
    ext: str = "/rpc/?v=5&type=search&arg="
    timeout: int = 3

homedir = os.environ['HOME']
whereami = homedir + "/.aurpm"
whereshouldpackagebe = 'null'
whereispackage = 'null'
giturl = 'null'
os.chdir(whereami)
print('my work dir ' + whereami)
workdir = whereami + '/work/'
enrepo = "yes"

if os.getuid() == 0:
    print("Oh welp, I've been given super powers! but with great power comes great privileges. Don't run AURPM with sudo")
    sys.exit(1)

helpmenu = """Useage: AURPM <operation> [...]
    AURPM -S 
    AURPM -h Help menu
    AURPM -i <package> Installs AUR packages, cannot search yet
    AURPM -ie <package> Installs AUR packages and allows editing of the PKGBUILD file
    AURPM -ce <package> complies the package and edits PKDBUILD
    AURPM -e <package> downloads the package and edits PKGBUILD
    AURPM -gpg <key> is a short cut fot gpg --search-keys
    """

def feedbackchecker(given):
    if given == []:
        print("The Package was not found or something went wrong!")
        sys.exit(1)
    else:
        print("The Package was found!")
given = []
packageaurname = []
def getaur(package):
    try:
        searchurl = aurinfo.url + aurinfo.ext + package
        print("using url: " + searchurl)
        with urlopen(searchurl, timeout=aurinfo.timeout) as feedback:
            given = (json.loads(feedback.read())['results'])
            print(given)
            packageaurname = (json.loads(given)['0'])
            print(packageaurname)
            print("All this does it print out the JSON is got from the AUR, this don't work yet!")

    except URLError:
        print("I don't think I'm connected to the internet. " + str(sys.exc_info()))
        sys.exit(2)
    except json.JSONDecodeError:
        print("I failed to decode the JSON I got! I cannot proceed, I shall exit. " + str(sys.exc_info()))
        sys.exit(2)

def complie(package, workdir):
    try:
        print("Complining the package")
        print(workdir)
        os.chdir(workdir)
        os.system("makepkg -sic")
        localrepo(package)
    except:
        print("Oh No! Something went wrong! " + str(sys.exc_info()))

def begins1(package):
    global giturl
    global workdir
    workdir = workdir + package
    giturl = "https://aur.archlinux.org/" + package + ".git"
    if giturl == 'null':
        print("Oh No! something went wrong! I didn't get the url for the AUR package!")
    else:
        print("I'm downloading the AUR package!")
        gitcloneresult = run(["git","clone",giturl,workdir], stdout=PIPE, stderr=STDOUT)
        print("sub-proccess log:")
        print(gitcloneresult)
        complie(package, workdir)

def gpg(key):
    print("This section is used for easy of access to installing gpg keys")
    os.system("gpg --search-keys " + key)
    print("Done!")

def begins2(package):
    global giturl
    global whereispackage
    global workdir
    workdir = workdir + package
    giturl = "https://aur.archlinux.org/" + package + ".git"
    if giturl == 'null':
        print("Oh No! something went wrong! I didn't get the url for the AUR package!")
    else:
        print("I'm downloading the AUR package!")
        gitcloneresult = run(["git","clone",workdir], stdout=PIPE, stderr=STDOUT)
        print("sub-proccess log:")
        print(gitcloneresult)
        print('opening the PKGBUILD file')
        whereispackage = whereami + package
        os.system('cd ' + whereispackage + ' && nano PKGBUILD')
        complie(package, workdir)

def localrepo(package):
    global whereispackage
    global whereami
    garb = 0
    if enrepo == 'yes':
        if os.path.exists(whereami + '/repo') == False:
            createrepo(whereami)
            print("the Repo directory wasn't found so one was created")
        # *.pkg.tar.zst
            os.chdir(workdir) 
        for roots,dirs,files in os.walk(workdir):
            fi = roots,files
            wildcard = '*.pkg.tar.zst'
            p1u = fnmatch.filter(files, '*.pkg.tar.zst')
            if p1u == []:
                garb += 1
            else:
                print('Match!')
                p2u = []
                p2u.append(roots + '/')
                rtxt1 = []
                rtxt1.append(p1u)
                p2u.append(p1u)
                rtxt1t = ''.join(map(str, rtxt1))
                p2us = ''.join(map(str, p2u))
                p2usr1 = p2us.replace('[', '', 2)
                p2usr2 = p2usr1.replace("'", '', 2)
                p2usr3 = p2usr2.replace("]", '', 2)
                print(p2usr3)
                os.chdir(whereami)
                os.system("bash -x repoadd1.sh " + p2usr3)

def pushrepo():
    if enrepo == 'yes':
        if os.path.exists(whereami + '/repo') == False:
            createrepo(whereami)
            print("the Repo directory wasn't found so one was created")
        os.chdir(whereami)
        print(os.system("bash -x uprepo.sh"))
    else:
        print('Local Repo disabled')



def pkgupdate():
    garb = 0
    print('updating all packages!')
    os.chdir(workdir)
    #os.remove("packages.txt") 
    for roots,dirs,files in os.walk(workdir):
        fi = roots,files 
        p1u = fnmatch.filter(files, '*.pkg.tar.zst')
        if p1u == []:
            garb += 1
        else:
            print('Match!')
            print(roots,p1u)
            p2u = []
            p2u.append(roots + '/')
            rtxt1 = []
            rtxt1.append(p1u)
            p2u.append(p1u)
            print(p2u)
            rtxt1t = ''.join(map(str, rtxt1))
            p2us = ''.join(map(str, p2u))
            p2usr1 = p2us.replace('[', '', 2)
            p2usr2 = p2usr1.replace("'", '', 2)
            p2usr3 = p2usr2.replace("]", '', 2)
            print(p2usr3)
            p2usr4 = '\n' + p2usr3
            #with open("packages.txt", "a") as pkginfo:
            #    pkginfo.write(p2usr4)
            #pkginfo.close()
            tmpfs1 = p2usr4.replace(workdir, '', 2)
            tmpfs2 = tmpfs1.replace(rtxt1t, '', 2)
            print(tmpfs2)
            tmpfs3 = tmpfs2.replace(tmpfs2 + '-', '', 1)
            print(tmpfs3)
            update = os.system('cd ' + roots + ' && git pull')
            if update == "Already up to date.":
                print("Not Calling pacman")
            else:
                os.system('cd ' + roots + ' && makepkg -sic')
    pushrepo()




def createrepo(whereami):
    os.chdir(whereami)
    os.mkdir('repo')

#if config['localrepo']['enable'] == 'yes':
#    if os.path.exists(whereami + '/repo') == False:
#        createrepo(whereami)
#        print("the Repo directory wasn't found so one was created")
#else:
#    print('Local Repo disabled')

try:
    # Look away! Spag code!
    if argv[1] == '-S':
        print("WIP")
        print("Searching the AUR")
        try:
            package = argv[2]
            pushrepo()
            #localrepo(package)
            #getaur(package)
        except IndexError:
            print("Oh No! you haven't told me what package you would like! I cannot search without this!!" + str(sys.exc_info()))
    elif argv[1] == '-h':
        print(helpmenu)
    elif argv[1] == '-u':
        pkgupdate()
    elif argv[1] == '-i':
        try:
            package = argv[2]
            begins1(package)
        except IndexError:
            print("Oh No! you haven't told me what package you would like!" + str(sys.exc_info()))
            print("Please state the package you want to install!")
            package = input("Package: ")
            begins1(package)
    elif argv[1] == 'r':
        pushrepo()
    elif argv[1] == 'rm':
        print("Not Working Yet!")

    elif argv[1] == '-ie':
        try:
            package = argv[2]
            begins2(package)
        except IndexError:
            print("Oh No! you haven't told me what package you would like!" + str(sys.exc_info()))
    elif argv[1] == '-e':
        #global whereispackage
        #global giturl
        package = argv[2]
        giturl = "https://aur.archlinux.org/" + package + ".git"
        print('Downloading the package!')
        gitcloneresult = run(["git","clone",giturl], stdout=PIPE, stderr=STDOUT)
        print("sub-proccess log:")
        print(gitcloneresult)
        print('opening the PKGBUILD file')
        whereispackage = whereami + package
        os.system('cd ' + whereispackage + ' && nano PKGBUILD')
        print('Exiting!')
        sys.exit(1)
    elif argv[1] == '-c':
        package = argv[2]
        complie(package)
    elif argv[1] == '-d':
        package = argv[2]
        giturl = "https://aur.archlinux.org/" + package + ".git"
        print('Downloading the package!')
        gitcloneresult = run(["git","clone",giturl], stdout=PIPE, stderr=STDOUT)
        print("sub-proccess log:")
        print(gitcloneresult)
        print('opening the PKGBUILD file')
        print('Exiting!')
        sys.exit(1)
    elif argv[1] == '-gpg':
        key = argv[2]
        gpg(key)
except IndexError:
    print("Oh No! something went wrong! have you tried AURPM -h yet? or have you forgot a argument?" + str(sys.exc_info()))
    print(helpmenu)
    print("Assuming you want to install a package!")
    package = input("Package: ")
    begins1(package)
except SystemExit:
    print("I have exited due to an issuse seen above")
