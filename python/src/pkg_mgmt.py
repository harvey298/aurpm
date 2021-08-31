# this is for basic pkg managment such as updating cleaning etc
import fnmatch,os

from subprocess import run, PIPE, STDOUT, Popen
from sys import stdout
from caution import caution, error, force_caution, force_error, info, force_info
from config_handler import req_conf
from index import index, testing_features, null_check



def pkg_update():
    workdir = req_conf("DEFAULT","work_dir")
    if workdir == "/tmp/aurpm/work/":
        error("Updating is disabled because of testing feature: "+testing_features.tmp_as_work,0)
        return
    else:
        garb = 0
        print('updating all packages!')
        os.chdir(workdir) 
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
                rtxt1t = ''.join(map(str, rtxt1))
                p2us = ''.join(map(str, p2u))
                p2usr1 = p2us.replace('[', '', 2)
                p2usr2 = p2usr1.replace("'", '', 2)
                p2usr3 = p2usr2.replace("]", '', 2)
                p2usr4 = '\n' + p2usr3
                tmpfs1 = p2usr4.replace(workdir, '', 2)
                tmpfs2 = tmpfs1.replace(rtxt1t, '', 2)
                tmpfs3 = tmpfs2.replace(tmpfs2 + '-', '', 1)
                os.system('cd ' + roots + ' && git pull')
                os.system('rm '+roots+"/*.pkg.tar.zst")
                os.system('cd ' + roots + ' && makepkg -sic')

def install_pkg(pkg):
    null_check(pkg,"Package Checking")
    giturl = "https://aur.archlinux.org/" + pkg + ".git"
    force_info("Downloading the AUR Package")
    workdir = req_conf("DEFAULT","work_dir")
    workdir2 = workdir
    workdir = workdir + pkg + "/"
    if req_conf("DEFAULT","testing") == True:
        if req_conf("TESTING","debug") == True:
            debug = True
        else: debug = False
    else: debug = False
    logs = run(["git","clone",giturl,workdir], stdout=PIPE, stderr=STDOUT)
    if debug == True:
        print(logs)
    #if "You appear to have cloned an empty repository" in logs.stdout:
    #    print("sadge")
    # Cleaning output!!
    logs = str(logs.stdout)
    logs = logs.replace('b"','',1)
    logs = logs.replace('"','',1)
    if "You appear to have cloned an empty repository" in logs:
        force_info("Removing current work directory! "+str(workdir))
        try:
            os.rmdir(workdir2 + pkg)
        except OSError:
            force_error("Unable to remove current working directory",0)
        force_error("This package doesn't exists! Exiting!",1)     
    print(logs)
    #rint(str(logs.stdout))
    os.chdir(workdir)
    os.system("makepkg -sic")

#install_pkg("uwufetch")
