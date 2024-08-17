from os.path import join, exists, abspath
from os import remove
from json import loads, dumps

from .shared import print_error, print_log

# Do not change default value. Trust me
DEFAULT_CONFIGURATION = {
    "AdditionalCreatePath": None,
}

config_path = abspath(join(__file__, "..", "config.json"))
REMOVE_KEY = "REMOVE"


def remove_duplicate(dict_a: dict, dict_b: dict):
    for key in dict_a.copy():
        value_a = dict_a.get(key)
        value_b = dict_b.get(key)
        if value_a != value_b and value_a != REMOVE_KEY:
            continue
        dict_a.pop(key)


def change_config(config):
    new_config_table = get_config()

    if config.additional_create_path:
        if config.additional_create_path == REMOVE_KEY:
            new_config_table["AdditionalCreatePath"] = REMOVE_KEY  # type: ignore the stupid dict[str, None]
        else:
            path = abspath(config.additional_create_path)
            if not exists(path):
                print_error(f"Invalid file/folder: '{path}'")
                return
            new_config_table["AdditionalCreatePath"] = path
            
    remove_duplicate(new_config_table, DEFAULT_CONFIGURATION)
    
    if len(new_config_table) <= 0:
        if exists(config_path):
            remove(config_path)
        return 

    with open(config_path, "wt") as file:
        print_log("Your new pygstudio configuration:")
        print(new_config_table)
        file.write(dumps(new_config_table))

def print_failed_config_details():
    print_log(f"Details: config_file={config_path}")

def get_config():
    new_config = DEFAULT_CONFIGURATION.copy()

    if not exists(config_path):
        return new_config

    with open(config_path, "r") as file:
        contents = file.read()
    try:
        new_config.update(loads(contents))
    except:
        print_error("The current configuration file is corrupted.")
        print_failed_config_details()

    return new_config
