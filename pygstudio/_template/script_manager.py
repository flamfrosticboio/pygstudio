# // Pygstudio template file created by pygstudio script (Version 1.2)
# ? You are free to edit this script

script_directory = "scripts"

import os
def run():
    import threading
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.abspath(current_directory)): return
    
    current_script_directory = current_directory + "\\" + script_directory
        
    threaded_filenames = os.listdir(current_script_directory)
    threaded_abspath =  script_directory.replace('/', '.').replace("\\", ".")
    for filename in threaded_filenames:
        if filename.startswith("_"): continue
        threading.Thread(daemon=True, target=exec, args=(
            f"import {threaded_abspath}.{filename.split('.')[0]}",)).start()