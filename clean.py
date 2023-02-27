from os import listdir,remove,getcwd
from os.path import isfile,join
import re

valid_folder = re.compile("[A-Z]+_\d\d\d\d_\d\d_\d\d")
here = getcwd()

folders = [f for f in listdir(here) if not isfile(join(here, f)) and valid_folder.match(f) ]
for folder in folders:
    for extension in ["aux", "log", "synctex.gz"]:
        to_be_removed = (here + '\\' + folder + "\\Jackmaguire." + extension)

        if isfile(to_be_removed):
            print("Removing: " + to_be_removed)
            try:
                remove(to_be_removed)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
                break