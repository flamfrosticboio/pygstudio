import sys, os; sys.path.append(os.path.abspath("./src"))   # to be executed inside workspace in terminal (not tests/)

import pygstudio
from pygstudio.globals import GameGlobals
from pygstudio.binds import BindFunctions

def on_exit():
    print("EXITING SELF")
    
def on_preinit():
    print("BEFORE WINDOW LOAD")
    
def on_preload():
    print("BEFORE EVENT LOOP")

BindFunctions.set_exit(on_exit) 
BindFunctions.set_preinit(on_preinit)
BindFunctions.set_preload(on_preload)

if __name__ == '__main__': 
    pygstudio.run((680, 420))