# 
# Copyright harvey298 2021 GPL
#
from colourlib import merge_format, format_reset
import sys

from util import get_install_status
def caution(warning):
    if get_install_status() == True:
        return
    print(merge_format("bold", "yellow")+"[Cauiton] "+format_reset(2)+warning+format_reset(0))

def error(error,status):
    if get_install_status() == True:
        return
    print(merge_format("bold", "red")+"[ERROR] "+format_reset(2)+str(error)+format_reset(0))
    if status == 0:
        return
    else:
        sys.exit(status)

def info(info):
    if get_install_status() == True:
        return
    print(merge_format("bold", "blue")+"[INFO] "+format_reset(2)+str(info)+format_reset(0))

def force_info(info):
    print(merge_format("bold", "blue")+"[INFO] "+format_reset(2)+str(info)+format_reset(0))

def force_caution(warning):
    print(merge_format("bold", "yellow")+"[Cauiton] "+format_reset(2)+warning+format_reset(0))

def force_error(error,status):
    print(merge_format("bold", "red")+"[ERROR] "+format_reset(2)+str(error)+format_reset(0))
    if status == 0:
        return
    else:
        sys.exit(status)
