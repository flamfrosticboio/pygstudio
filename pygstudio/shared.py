from os.path import isdir, join, dirname
from zipfile import ZipFile

def get_user_choice():
    choice = input("> (y/n): ")
    if choice.lower().startswith("y"):
        return True
    elif choice.lower().startswith("n"):
        return False
    return get_user_choice()

def print_error(message):
    print("\033[31m"+message+"\033[0m")
    
def print_warning(message):
    print("\033[93m"+message+"\033[0m")
    
def print_log(message):
    print("\033[34m"+message+"\033[0m")
    
def print_success(message):
    print("\033[92m"+message+"\033[0m")
    
def unzip_contents(folder, zipfile):
    if not isdir(folder):
        template_zip = join(dirname(folder), zipfile)
        with ZipFile(template_zip, "r") as zip_ref:
            zip_ref.extractall(folder)