import sys, os; sys.path.append(os.path.abspath("./src"))   # to be executed inside workspace in terminal (not tests/)

import pygstudio


if __name__ == '__main__': 
    pygstudio.run((680, 420))