#! /bin/bash
#TODO should change zingales such that you set up github username via settings file
if [ -f ~/.ssh/id_rsa.pub ]; then
  :
else
  #this machine doesn't have a key
  echo "We are going to generate a ssh key"
  ssh-keygen
fi

#test if you your git stuffs is configured correctly
echo "test if this machine has ssh keys work with github"
ssh -T git@github.com
