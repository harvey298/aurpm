import configparser,os
from re import search

from index import config_default_keys, config_testing_keys, index, possible_config_locations
from colour_lib import error,caution,info

config = configparser.ConfigParser()

class default_config:
    DEFAULT: str = config_default_keys
    TESTING: str = config_testing_keys


def check_conf(conf_location):
    config.read(conf_location)
    conf = config.sections()
    if "work_dir" in config['DEFAULT']:
        return True
    else:
        return False
    
    if config.get('TESTING','multi_thread_update'):
        print("Yes") 

def search_config():
    if os.path.isfile(possible_config_locations.recommended_conf_location):
        info("Using config "+possible_config_locations.recommended_conf_location)
        return possible_config_locations.recommended_conf_location

    elif os.path.isfile(possible_config_locations.user_conf_1):
        info("Using config "+possible_config_locations.user_conf_1)
        return possible_config_locations.user_conf_1

    else:
        info("No Physical Config found! Falling back to internal config")
        return True

def req_conf(section,key):
    res = search_config()
    #print(res)
    if res == True:
        if section == "DEFAULT":
            if key == "work_dir":
                return config_default_keys.work_dir
        elif section == "TESTING":
            return True
    else:
        config.read(res)
        #print(res)
        #print(config["DEFAULT"]["TESTING"])
        if config["DEFAULT"].getboolean("TESTING") == True:
            info("Testing is enabled!")
            if config["TESTING"].getboolean("use_tmp_as_work") == True:
                caution("Updating is disabled!")
                if key == "work_dir":
                    try:
                        os.mkdir("/tmp/aurpm")
                    except FileExistsError:
                        pass
                    
                    try:
                        os.mkdir("/tmp/aurpm/work/")
                    except FileExistsError:
                        pass

                    return "/tmp/aurpm/work/"
        else:
            if "$HOME" in config[section][key]:
                var = config[section][key].replace("$HOME",index.home)
                var = var.replace('"','',2)
            return var


#print(req_conf("DEFAULT","work_dir"))