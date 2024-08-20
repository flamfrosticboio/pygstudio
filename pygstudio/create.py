from shutil import rmtree, copytree, copy
from os.path import abspath, dirname, exists, isdir, isfile, join

from .shared import *
from .config import get_config, print_failed_config_details

_ignore_dir = lambda *args, **kwargs: ["__pycache__"]


def main(output_folder, output_name, flags):
    output_folder = join(abspath(output_folder), output_name)
    template_folder = join(dirname(abspath(__file__)), "template")

    if exists(output_folder):
        if flags.confirm == False:
            print_warning("Warning: The project exists! Overwrite?")
            choice = get_user_choice()
            if choice == False:
                return print_error("Operation is cancelled!")
        rmtree(output_folder)

    unzip_contents(template_folder, "template.zip")
    copytree(template_folder, output_folder, ignore=_ignore_dir)
    main_file_directory = join(output_folder, "main.py")

    with open(main_file_directory, "rt") as main_file:
        contents = main_file.read().replace("$MYPYGSTUDIOGAME", output_name)

    with open(main_file_directory, "wt") as main_file:
        main_file.write(contents)

    config_table = get_config()
    if (filepath := config_table.get("additional_create_path", None)) is not None and flags.exclude_additional_files is False:
        if isfile(filepath):
            copy(filepath, output_folder)
        elif isdir(filepath):
            copytree(filepath, output_folder, dirs_exist_ok=True)
        else:
            print_error(
                "PygstudioConfigError: Invalid path for configuration 'additional_create_path'. Skipping process!"
            )
            print_failed_config_details()

    print_success(
        f"Successfully created a new Pygstudio project at '{abspath(dirname(output_folder))}'"
    )
