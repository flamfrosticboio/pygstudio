from os.path import join, exists, abspath
from os import remove
from json import loads, dumps

from .shared import *

config_path = abspath(join(__file__, "..", "config.json"))

# Do not change default value to often. Trust me
DEFAULT_CONFIGURATION = {
    "additional_create_path": None,
    "default_pyinstaller_args": "-w --noconfirm",
}

def print_table_line(key, value):
    print(f"| \033[93m{key}\033[0m = \033[34m{repr(value)}\033[0m")

def print_table(table):
    for key in table:
        print_table_line(key, table.get(key))

failed_details_text = f"""Details: 
config_file={config_path}"""
def print_failed_config_details():
    print_log(failed_details_text)
    print_table(get_config())


def save_configuration(new_config_table):
    if len(new_config_table) <= 0:
        if exists(config_path):
            remove(config_path)
        return

    with open(config_path, "wt") as file:
        print_log("Your new pygstudio configuration:")
        print_table(new_config_table)
        file.write(dumps(new_config_table))


def change_configuration(config):
    new_config_table = get_config()

    for key in DEFAULT_CONFIGURATION:
        if not getattr(config, key):
            continue
        new_config_table[key] = getattr(config, key)

    save_configuration(new_config_table)


def get_configuration(config):
    table = get_config()

    print_success(f"config_path={config_path}")
    print_log("Your configuration table:")

    keys = {key for key in DEFAULT_CONFIGURATION if getattr(config, key, False) == True}
    print_table(table if len(keys) == 0 else keys)


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

def reset_config(config):
    table = get_config()

    print_success(f"config_path={config_path}")
    
    for key in DEFAULT_CONFIGURATION:
        if not getattr(config, key):
            continue
        table[key] = DEFAULT_CONFIGURATION[key]
    
    save_configuration(table)

def main(config):
    if config.config_command == "set":
        change_configuration(config)
    elif config.config_command == "get":
        get_configuration(config)
    elif config.config_command == "remove":
        reset_config(config)
    else:
        print_error("No arguments provided. Type `pygstudio config -h` for help.")