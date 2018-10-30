
################################################################

import os

################################################################

print('------------- find_same_dir -------------')

dirmap = dict()
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    dirkey = os.path.basename(dirpath)

    if dirkey not in dirmap.keys():
        dirmap[dirkey] = list()

    dirmap[dirkey].append(dirpath)

for dirkey, dirlist in dirmap.items():
    if len(dirlist) > 1:
        print(dirlist)

print('------------------ END ------------------')

################################################################
