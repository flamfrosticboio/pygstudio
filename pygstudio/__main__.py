import sys, argparse

__all__ = ["__version__", "__pygstudio_version__"]
__pygstudio_version__ = "1.1"
__version__ = "1.1"


def warn(message):
    print("\033[93m" + message + "\033[0m")


if sys.version_info < (3, 8, 0):
    warn(
        "[Warning]: Pygstudio may not work as intended in lower versions of python. "
        "It is recommended to have python 3.8.0 or above!"
    )

DEFAULT_RELEASE_OPTIONS = "-w --noconfirm"

NOTES = """
@ Flamfrosticboio
Developer-Notes:

`python -m pygstudio release --optimize-storage`
`python -m pygstudio release -s`
- This enables storage optimization by removing redundant dlls
- Your game might break if some dlls are removed from the game. Use it as your own risk.
"""


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

    subparser = main_parser.add_subparsers(dest="command")
    create_parser = subparser.add_parser(
        "create", help="creates a new pygstudio project from template"
    )
    release_parser = subparser.add_parser(
        "release", help="makes a pygstudio project made for release"
    )
    config_parser = subparser.add_parser("config", help="configure pygstudio behavior. pass 'REMOVE' to remove that configuration")

    create_parser.add_argument("name", type=str, help="name of the project")
    create_parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=".",
        help='the output directory of the project (default=".")',
    )

    release_parser.add_argument(
        "-f", "--folder", type=str, help="the project directory to release", default="."
    )
    release_parser.add_argument(
        "-o", "--output", type=str, help="the output of the project", default=".dest"
    )
    release_parser.add_argument(
        "-x",
        "--options",
        type=str,
        help="options for pyinstaller",
        default=DEFAULT_RELEASE_OPTIONS,
    )
    release_parser.add_argument(
        "-s",
        "--optimize-storage",
        action="store_true",
        help="enable storage optimization. Read more by calling `python -m pygstudio --notes`",
    )
    release_parser.add_argument(
        "-c",
        "--no-confirm",
        action="store_true",
        help="skips the overwrite confirmation",
    )

    config_parser.add_argument(
        "--additional-create-path",
        help="Path that include folders/files to the new project when `pygstudio create` is called.",
        type=str
    )

    return main_parser


def main():
    user_args = initialize_parsers().parse_args()
    if not any(vars(user_args).values()):
        sys.exit("No arguments provided. Type `pygstudio -h` for help.")
    elif user_args.notes:
        print(NOTES)
    elif user_args.command == "release":
        from .release import release_item

        release_item(
            user_args.folder, user_args.output, user_args.options, flags=user_args
        )
    elif user_args.command == "create" and user_args.name:
        from .create import main

        main(user_args.output, user_args.name)
    elif user_args.command == "config":
        from .config import change_config
        
        change_config(user_args)


if __name__ == "__main__":
    main()
