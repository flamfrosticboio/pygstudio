from os.path import abspath, basename, join, exists
from os import makedirs, listdir, walk, remove
from subprocess import call
from shutil import rmtree, move, copytree
from . import shared

COMMAND_LINE = """cmd /C pyinstaller "{file_name}" -D --name "{game_name}" \
--specpath "{temp_folder}" --distpath "{output_folder}" --workpath "{temp_folder}" \
{other_args}
"""

INSTALLER_FOLDER = join(__file__, "..", "installer")


def optimize_dlls(internal_folder):
    for dirpath, _, filenames in walk(internal_folder):
        if dirpath == internal_folder:
            continue
        for filename in filenames:
            if filename.endswith(".dll"):
                remove(join(dirpath, filename))


def release_item(source_folder, output_folder, other_args: str, flags):
    source_folder = abspath(source_folder)
    output_folder = abspath(output_folder)

    if exists(output_folder) and len(listdir(output_folder)) > 0:
        if flags.confirm == False:
            shared.print_warning(
                "Warning: The release folder has some contents that will be overwritten! Continue?"
            )
            choice = shared.get_user_choice()
            if choice == False:
                return print("Operation is cancelled!")
        rmtree(output_folder)

    game_name = basename(source_folder)
    temp_folder = join(output_folder, ".build")
    if not exists(temp_folder):
        makedirs(temp_folder)

    main_file = join(source_folder, "main.py")
    if not exists(main_file):
        main_file = join(source_folder, game_name + ".py")
    if not exists(main_file):
        raise RuntimeError(
            "Main file is not found. Consider renaming the main file to `main.py` or your <game_name>.py"
        )

    details = COMMAND_LINE.format(
        source_folder=source_folder,
        game_name=game_name,
        temp_folder=temp_folder,
        output_folder=output_folder,
        other_args=other_args,
        file_name=main_file,
    )

    result = call(details)
    rmtree(temp_folder)

    if result != 0:
        exit("\033[91mPygstudio: An error occured in pyinstaller.\033[00m")

    move(join(output_folder, game_name, "_internal"), output_folder)
    move(join(output_folder, game_name, game_name + ".exe"), output_folder)
    rmtree(join(output_folder, game_name))

    source_assets = join(source_folder, "assets")
    if len(listdir(source_assets)) > 0:
        copytree(source_assets, join(output_folder, "assets"))

    if flags.optimize_storage:
        from .shared import print_warning

        optimize_dlls(join(output_folder, "_internal"))
        print_warning(
            "Warning: Some dll's are removed. Expect for the program to crash at some point.\n"
            "Remove the argument `-s/--optimize-storage` to stop removing dlls."
        )
