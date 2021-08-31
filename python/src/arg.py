import sys
from colour_lib import error
from pkg_mgmt import install_pkg

def request_pkg_mgmt(argument):
    if argument == 'S':
        try:
            pkg = sys.argv[2]
            install_pkg(str(pkg))
        except IndexError:
            error("Oops!! you haven't told me a pkg to install!!")
def handle():
    try:
        if '-' in sys.argv[1]:
            argument = sys.argv[1]
            argument = argument.replace('-','',1)
            if 'S' in argument:
                request_pkg_mgmt(argument)
        else:
            error("I don't know what todo!! try -h (for help)")
    except IndexError:
        error("I don't know what todo!! try -h (for help)")

#handle()