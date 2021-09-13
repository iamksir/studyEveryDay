import os
import glob

path = glob.glob('*.png')
for x in path:
    path_splitext = os.path.splitext(x)
    print(path_splitext)