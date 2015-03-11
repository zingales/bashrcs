#! /bin/bash
#TODO should change zingales such that you set up github username via settings file
if [ -f ~/.ssh/id_rsa.pub ]; then
  :
else 
  #this machine doesn't have a key
  echo "We are going to generate a ssh key"
  ssh-keygen
  curl -u "zingales@mit.edu" --data '{"title":\"`hostname`\","key":\"`cat ~/ssh/id_rsa.pub`\"}' https://api.github.com/user/keys

fi 

#test if you your git stuffs is configured correctly
ssh -T git@github.com
if [ $? -eq 0 ]; then
  #add code to upgrade your https://remote repo to git@github. So we don't have to worry about adding in our username and what not
  :
else
  echo "failed to access github"
fi
