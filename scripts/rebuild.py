import os, shutil, subprocess

pygstudio = os.path.dirname(os.path.dirname(__file__))
directories =  ["build", "dist", "pygstudio.egg-info"]
for item in directories:
    path = os.path.join(pygstudio, item)
    if not os.path.exists(path): continue
    shutil.rmtree(path, ignore_errors=True)
subprocess.call("cmd /C python -m build")