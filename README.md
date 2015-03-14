bashrcs
=======

A onestop shop for setting up your enviroment, you set it up once, and then you can basically set up your enviroment / keep it up to date no problem on all your machines. 




Installation
============
There are two steps, downloading your version of this repo, and running it. 

Downloading this version of your repo can kinda of be a catch-22 if you don't have git / your ssh keys installed. So i've provided a bootstrap.sh which you can wget from your repo and then run it wich will handle the catch-22 problem of not having git / ssh keys. 


Otherwise you can git clone your repo into any folder. 

Once you have your repo cloned you can run ./install which might ask you a couple questions, about how you want the username installed and if you follow what it says you should have an up and running system when your done. 


Customizing for your setup
============

there are a couple of things you have to modify, over time i will try to fix such that there is only one file but for now:

File one is the install_setttings.json: 
---------------------------------------

this has three types of lines: git_ensure lines, cd_install lines, and _other_ lines. 

git_ensure
----------

the git_ensure array will use the following args to git_ensure, which either clones the repo if it doesn't exist, and git pull's if it does exist. 

cd_install
----------

This will create cd_install scripts, in the scripts folder. Basically it will cd into a folder, run the command, force means if you should rerun during every install or just during the first time. This is useful if a command is not idempotent. 

Other
-------

If it finds a file by this name inside the files folder, it will apply this rules somewhere. There are some keyword saved args mainly

\_comment : which is just for descriptions sake

to_save : these are files that should be "saved" regardles of if they are going to be replaced

to_ignore: these are files that shouldn't be copied to even if they exist in the files folder

Next files to modify:
--------------------- 

All the requirements file, depending on what you use.

brew is for OSX Homebrew

apt-get is for Ubuntu apt-get 

pip is for python pip 


