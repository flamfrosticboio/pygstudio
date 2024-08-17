# // Pygstudio template file created by pygstudio script (Version 1.3.1)
# ? You are free to edit this script

script_directory = "scripts"

from os.path import dirname, abspath, join, exists
from os import listdir
def run():
    import threading
    
    current_directory = dirname(abspath(__file__))
    current_script_directory = join(current_directory, script_directory)
    if not exists(abspath(current_script_directory)): return
        
    threaded_filenames = listdir(current_script_directory)
    threaded_abspath =  script_directory.replace('/', '.').replace("\\", ".")
    for filename in threaded_filenames:
        if filename.startswith("_"): continue
        threading.Thread(daemon=True, target=exec, args=(
            f"import {threaded_abspath}.{filename.split('.')[0]}",)).start()