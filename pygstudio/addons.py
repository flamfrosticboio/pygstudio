from os.path import abspath, join, exists, isdir
from os import listdir, makedirs
from shutil import copy
from .shared import *


def main(args):
    if args.addon_command == "list":
        list_addons()

    elif args.addon_command == "add":
        output = abspath(args.output)
        if not exists(output) or not isdir(output):
            print_error(f"Output directory not found '{output}'. Operation Aborted!")
            return
        extract_addons(add_addon(args, output))
        print_success(f"Successfully added addons to '{output}'")


def list_addons():
    from .shared import print_success

    addons = get_addons()

    print_success("Built-in addons avaliable:")
    for name, desc in addons.items():
        print(f"* \033[93m{name}\033[0m{' ' * (max(15-len(name), 0)+1)}{desc}")


def read_firstline_doc(filepath):
    if not exists(filepath):
        return ""

    with open(filepath, "rt") as file:
        return file.readline().replace('"""', "").strip()


def extract_addons(callback):
    from tempfile import TemporaryDirectory
    from .shared import unzip_contents

    with TemporaryDirectory() as temp_dir:
        unzip_contents(abspath(join(__file__, "..", "addons.zip")), temp_dir)
        return callback(temp_dir)


def _get_addons(temp_dir):
    return {
        name.split(".")[0]: read_firstline_doc(abspath(join(temp_dir, name + "i")))
        for name in listdir(temp_dir)
        if name.endswith(".py")
    }


def get_addons():
    return extract_addons(callback=_get_addons)


def add_addon(args, output):
    def wrapper(temp_dir):
        avaliable = set(
            name.split(".")[0] for name in listdir(temp_dir) if name.endswith(".py")
        )
        for addon in args.items:
            if addon in avaliable:
                copy(
                    abspath(join(temp_dir, addon + ".py")),
                    abspath(join(output, addon + ".py")),
                )
                if exists(path := abspath(join(temp_dir, addon + ".pyi"))):
                    copy(path, abspath(join(output, addon + ".pyi")))
            else:
                print_warning(
                    f"Could not find addon '{addon}'. Skipping adding this process"
                )

    return wrapper
