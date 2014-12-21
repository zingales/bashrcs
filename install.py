import os
import time
import shutil
from os import walk
import json
import subprocess

#Global Vars
homedir = os.path.expanduser("~")+"/"
installdir=os.path.dirname(os.path.abspath(__file__))
# to_ignore = ['.DS_Store']
# toMove = [".gitconfig"]



# modifyig this argument will have no affect, its overwritten in run
to_ignore = []
old_rcs = ""

def _run_cmd(cmd):
    try:
        return subprocess.check_output(cmd , stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        print e.output
        raise

def git_ensure(folder, url):
    print _run_cmd("~/scripts/ensure_git %s %s" % (folder, url))
    #print subprocess.check_output, stderr=subprocess.STDOUT, shell=True)
    pass

def cd_install(name, folder, cmd, reinstall=False):
    print _run_cmd(installdir+"/cd_install.sh %s %s %s" % (name, folder, cmd))
    #print subprocess.check_output("install_scripts/cd_install.sh %s %s %s" % (name, folder, cmd), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    pass

def guarantee_folder(folder):
    if folder == homedir:
        return
    if not os.path.exists(folder):
        os.makedirs(folder)

def save(path, isFolder=False):
    guarantee_folder(old_rcs)
    if not os.path.exists(path):
        return
    print "copying existant ", path, " to " +old_rcs
    name = os.path.basename(path)

    to_ignore
    if isFolder:
        shutil.copytree(path, old_rcs+"/"+name, ignore=shutil.ignore_patterns(*to_ignore))
    else:
        name = name.replace(".", "")
        shutil.copy(path, old_rcs+"/"+name)

def install_file(filename, file_set):
    if file_set.get("ignore", False) or filename in to_ignore:
        return
    folder = file_set.get("install_dir", "~")
    folder = folder.replace("~", homedir)
    guarantee_folder(folder)
    dest = folder+file_set.get("install_name", "."+filename)
    if file_set.get("save_original", True):
        save(dest)
    shutil.copy("files/"+filename, dest)

def install_folder(foldername, folder_set):
    if folder_set.get("ignore", False) or foldername in to_ignore:
        return
    folder = folder_set.get("install_dir", "~")
    folder = folder.replace("~", homedir)

    if folder_set.get("save_original", True):
        save(folder, isFolder=True)
    guarantee_folder(folder)

    src_folder = "files/"+foldername
    for filename in os.listdir(src_folder):
        shutil.copy(src_folder+"/"+filename, folder+'/'+filename)

def run():
    settings = {}
    files_to_install = []
    folders_to_install = []

    #generate time as a string that can exist as a folder name
    temp_name = time.ctime()
    temp_name = temp_name.replace(" ", '_')
    temp_name = temp_name.replace(":", "_")

    global old_rcs
    old_rcs = "oldrcs/" + temp_name

    if not os.path.exists(homedir+".bash_profile"):
        print "Your really gonna need a bash_profile"


    #load file settings
    with open("install_settings.json", 'r') as jsonFile:
        settings = json.loads(jsonFile.read())

    global to_ignore
    to_ignore = settings.get("to_ignore", [".DS_Store"])

    ##### Copy Files and Folder #######
    #saving specific files not in ./files
    for original_file in settings.get("to_save", []):
        save(original_file)

    #load all files and directores in ./files
    for (dirpath, dirnames, filenames) in walk("./files"):
        if (dirpath == "./files"):
            files_to_install = filenames
            folders_to_install = dirnames

    for filename in files_to_install:
        install_file(filename, settings.get(filename, {}))

    for foldername in folders_to_install:
        install_folder(foldername, settings.get(foldername, {}))
    ##### End Copy Files and Folder #######

    ##### Ensure Git / install ######
    for cmds in settings.get('git_ensure', []):
        git_ensure(cmds["folder"], cmds["url"])

    for cmds in settings.get("cd_install", []):
        cd_install(cmds["name"], cmds["folder"], '"' + cmds["cmd"]+'"')

    ##### end Ensure Git / install ######

if __name__ == "__main__":
    run()
