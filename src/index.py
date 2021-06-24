import os
global silence_install

from caution import error

class index:
    home: str = os.environ['HOME']

class config_default_keys:
    work_dir: str = index.home+"/.aurpm/work/" 
    testing: bool = False

class config_testing_keys:
    multi_thread_update: str = False
    use_tmp_as_work: str =  False


class possible_config_locations:
    system_conf: str = False
    user_conf_1: str = index.home+"/.config/aurpm/aurpm.conf"

    user_conf_2: str = index.home+"/.aurpm/aurpm.conf"
    
    recommended_conf_location: str = user_conf_2

class testing_features:
    tmp_as_work: str = "/tmp as work directory"
    multi_thread_update: str =  "Multi-Thread updating (Not Implemented)"

def null_check(var,state):
    if var == "null":
        error("Oh No I didn't get the correct data! more info: "+str(state))
        return False