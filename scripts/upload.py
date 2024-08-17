import subprocess, sys
import rebuild

RED = "\033[91m"
RESET  = "\033[00m"

result = subprocess.call("cmd /C python -m twine check dist/*")
if result != 0:
    print(RED + "TwineVertificationError: An error occured during vertification process. Aborting upload!"+ RESET)
    sys.exit(-1)
    
subprocess.call("cmd /C python -m twine upload dist/*")