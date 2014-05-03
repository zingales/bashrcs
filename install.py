import os
import time
import shutil
from os import walk

#Global Vars
homedir = os.path.expanduser("~")+"/"
to_ignore = ['.DS_Store']
toMove = [".gitconfig"]

#genearte time as a string that can exist as a folder name
temp_name = time.ctime()
temp_name = temp_name.replace(" ", '_')
temp_name = temp_name.replace(":", "_")
old_rcs = "oldrcs/" + temp_name


def guarantee_folder(folder):
	if not os.path.exists(folder):
		os.makedirs(folder)

def save(filepath):
	guarantee_folder(old_rcs)
	print "copying existant ", filepath, " to " +old_rcs
	name = os.path.basename(filepath).replace(".", "")
	shutil.copy(filepath, old_rcs+"/"+name)

def install(filename, dest=homedir):
	shutil.copy("files/"+filename, dest+"/."+filename)

def run():
	toInstallraw = []
	for (dirpath, dirnames, filenames) in walk("./files"):
	    if (dirpath == "./files"):
        	toInstallraw.extend(filenames)

	for x in to_ignore:
		if x in toInstallraw:
			toInstallraw.remove(x)

	toCheck = ["."+x for x in toInstallraw]

	for filename in os.listdir(homedir):
		if filename in toCheck:
			toMove.append(filename)
		

	for fileToMove in toMove:
		save(homedir+fileToMove)

	for fileToInstall in toInstallraw:
		install(fileToInstall)

if __name__ == "__main__":
	run()
