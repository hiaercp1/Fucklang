import sys
import os.path

def parse_arguments():
    if len(sys.argv) == 1:
        return False
    elif os.path.isfile(sys.argv[1]) == False:
        return False
    return sys.argv[1]
