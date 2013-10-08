import os
import time
import shutil
from os import walk

homedir = os.path.expanduser("~")+"/"


toInstallraw = []
for (dirpath, dirnames, filenames) in walk("./files"):
    toInstallraw.extend(filenames)

if ".DS_Store" in toInstallraw:
	toInstallraw.remove(".DS_Store")
toInstall = ["."+x for x in toInstallraw]

#genearte time as a string that can exist in a filder
temp_name = time.ctime()
temp_name = temp_name.replace(" ", '_')
temp_name = temp_name.replace(":", "_")
old_rcs = "oldrcs_" + temp_name

# print homedir
# print toInstall
toMove = []

for filename in os.listdir(homedir):
	if filename in toInstall:
		print "moving existant ", filename, " to " +old_rcs
		toMove.append(filename)



#genearte temporary folder name
if toMove:
	os.makedirs(old_rcs)

for fileToMove in toMove:
	shutil.move(homedir+fileToMove, old_rcs+"/"+fileToMove.replace(".",""))

for fileToInstall in toInstallraw:
	shutil.copy("files/"+fileToInstall, homedir+"/."+fileToInstall)
# print toMove
