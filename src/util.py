import os,sys

# this file is ONLY for 2 imports this prevents circular importing!!

def permission_check():
    if os.getuid() == 0:
        print("Oh welp, I've been given super powers! but with great power comes great privileges. Don't run AURPM with sudo")
        sys.exit(1)

def get_install_status():
    try:
        if sys.argv[1] == "-i":
            return True
        else:
            return False
    except IndexError:
        return False