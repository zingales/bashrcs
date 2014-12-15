#! /bin/bash

NAME=$1
DIR=$2
CMD=$3
INST=le_installed

if [ -d $DIR ]; then
  if [ -a $INST ]; then
      echo $NAME "installed"
  else
      cd $DIR
      eval $CMD
      touch $INST
      echo $NAME "installed"
  fi;
fi;
