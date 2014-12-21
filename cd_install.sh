#! /bin/bash

NAME=$1
DIR=$2
CMD=$3
INST=".le_installed"

if [ -d $DIR ]; then
  cd $DIR
  if [ -a $INST ]; then
      echo "$NAME installed"
  else
      eval $CMD
      touch $INST
      echo "$NAME installed"
  fi;
fi;
