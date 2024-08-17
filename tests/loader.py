from os.path import abspath, join
from importlib import util
import sys

def load_module(module_name: str):
    spec = util.spec_from_file_location(module_name, abspath(join(__file__, "..", "..", "pygstudio", module_name+".py")))
    if not spec: raise RuntimeError(f"Module not found: {module_name}")
    if not spec.loader: raise RuntimeError("Something went wrong when loading spec.loader")
    module = util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module