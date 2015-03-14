#! /bin/bash

if [ -z $1 ]; then
  echo "you need to provide a git url as an argument (the version which includes https:// rather than git@github"
  exit
fi

which brew 
if [ $? -eq 0 ]; then
  #this machine has brew running
  echo "We are going to brew install git"
  brew update
  for pkg in git; do
      if brew list -1 | grep -q "^${pkg}\$"; then
        :
      else
          brew install $pkg
      fi
  done
fi 

which apt-get
if [ $? -eq 0 ]; then
  #this machine has apt-get
  echo "We are going to sudo apt-get install git"
  sudo apt-get update
  sudo apt-get -y install git
fi 

git clone $1
