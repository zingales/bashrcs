#! /bin/bash
#ensure gat is up to date
ensure_git ~/.gat https://github.com/zingales/gat.git 

#copy gat script to scripts folder
cd ~/.gat
cp ex_gat_script ~/scripts/gat
