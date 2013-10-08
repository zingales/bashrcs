import os
import time
import shutil
from os import walk

homedir = os.path.expanduser("~")+"/"


toInstallraw = []
for (dirpath, dirnames, filenames) in walk("./files"):
    toInstallraw.extend(filenames)

toInstall = ["."+x for x in toInstallraw]


print homedir
print toInstall
toMove = []

for filename in os.listdir(homedir):
	if filename in toInstall:
		print "i exist", filename
		toMove.append(filename)

#genearte time as a string that can exist in a filder
temp_name = time.ctime()
temp_name = temp_name.replace(" ", '_')
temp_name = temp_name.replace(":", "_")

#genearte temporary folder name
if toMove:
	old_rcs = "oldrcs_" + temp_name
	os.makedirs(old_rcs)

for fileToMove in toMove:
	shutil.move(homedir+fileToMove, old_rcs+"/"+fileToMove.replace(".",""))

for fileToInstall in toInstallraw:
	shutil.copy("files/"+fileToInstall, homedir+"/."+fileToInstall)
print toMove
