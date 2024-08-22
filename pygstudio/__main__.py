import sys, argparse

__all__ = ["__version__", "__pygstudio_version__"]
__pygstudio_version__ = "1.1a1"
__version__ = "1.1"


def warn(message):
    print("\033[93m" + message + "\033[0m")


if sys.version_info < (3, 8, 0):
    warn(
        "[Warning]: Pygstudio may not work as intended in lower versions of python. "
        "It is recommended to have python 3.8.0 or above!"
    )

NOTES = """
@ Flamfrosticboio
Developer-Notes:

`python -m pygstudio release --optimize-storage`
`python -m pygstudio release -s`
- This enables storage optimization by removing redundant dlls
- Your game might break if some dlls are removed from the game. Use it as your own risk.
"""

from .config import DEFAULT_CONFIGURATION, get_config

# The order of helps must be the same as DEFAULT_CONFIGURATION
_helps = [
    "Path that include folders/files to the new project when `pygstudio create` is called.",
    "Default pyinstaller args that is combined with 'pygstudio release -x'",
]
configs = zip(DEFAULT_CONFIGURATION, _helps)

assert len(DEFAULT_CONFIGURATION) == len(_helps)


def initialize_create_parsers(subparser):
    create_parser = subparser.add_parser(
        "create", help="creates a new pygstudio project from template"
    )

    create_parser.add_argument("name", type=str, help="name of the project")
    create_parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=".",
        help='the output directory of the project (default=".")',
    )
    create_parser.add_argument(
        "-c", "--confirm", action="store_true", help="skips prompt for overwrite"
    )
    create_parser.add_argument(
        "-x",
        "--exclude-additional-files",
        action="store_true",
        help="Excludes additional files that may be added in the project.",
    )


def initialize_release_parsers(subparser):
    release_parser = subparser.add_parser(
        "release", help="makes a pygstudio project made for release"
    )

    release_parser.add_argument(
        "-f", "--folder", type=str, help="the project directory to release", default="."
    )
    release_parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="the output folder for the released game",
        default="./release",
    )
    release_parser.add_argument(
        "-x",
        "--options",
        type=str,
        help="options for pyinstaller",
        default="",
    )
    release_parser.add_argument(
        "-s",
        "--optimize-storage",
        action="store_true",
        help="enable storage optimization. Read more by calling `python -m pygstudio --notes`",
    )
    release_parser.add_argument(
        "-c",
        "--confirm",
        action="store_true",
        help="skips the overwrite confirmation",
    )


def initialize_config_parsers(subparser):
    config_parser = subparser.add_parser(
        "config",
        help="configure pygstudio behavior.",
    )

    config_sub_parser = config_parser.add_subparsers(dest="config_command")

    config_set = config_sub_parser.add_parser("set", help="sets a configuration")
    config_get = config_sub_parser.add_parser("get", help="gets a configuration")
    config_remove = config_sub_parser.add_parser(
        "remove", help="resets a configuration"
    )

    for command, help in configs:
        command = "--" + command.replace("_", "-")
        config_set.add_argument(command, help=help, type=str, default=None)
        config_get.add_argument(command, help=help, action="store_true")
        config_remove.add_argument(command, help=help, action="store_true")


# Placed in a seperate function just to close/fold this monstrosity
def initialize_parsers():
    main_parser = argparse.ArgumentParser(
        prog="pygstudio",
        description="A cli to easily create pygstudio based games. Addition notes can be found by calling `python -m pygstudio --notes`",
        epilog="@ pygstudio v1.1 by flamfrosticboio",
    )

    main_parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="prints the version of pygstudio and cli",
        version=f"pygstudio {__pygstudio_version__} (cli version: {__version__})",
    )

    main_parser.add_argument(
        "-n",
        "--notes",
        action="store_true",
        help="Print some notes that the developer may include.",
    )

    main_parser.add_argument(
        "--path",
        help="Print the path of pygstudio folder",
        action="store_true",
    )

    subparser = main_parser.add_subparsers(dest="command")
    initialize_create_parsers(subparser)
    initialize_release_parsers(subparser)
    initialize_config_parsers(subparser)

    return main_parser


def main():
    user_args = initialize_parsers().parse_args()
    if not any(vars(user_args).values()):
        from .shared import print_error

        print_error("No arguments provided. Type `pygstudio -h` for help.")
        sys.exit(0)
    elif user_args.notes:
        print(NOTES)
    elif user_args.path:
        from os.path import dirname

        print("Pygstudio path:", dirname(__file__))
    elif user_args.command == "release":
        from .release import release_item

        release_item(
            user_args.folder, user_args.output, user_args.options, flags=user_args
        )
    elif user_args.command == "create" and user_args.name:
        from .create import main

        main(user_args.output, user_args.name, user_args)
    elif user_args.command == "config":
        from .config import main

        main(user_args)


if __name__ == "__main__":
    main()
