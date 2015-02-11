# if you don't have a .bash_profile you need this so it 
# automagiaclly loads your .bashrc if one exists otherwise
# just add this line to your current profile rc but you 
# shouldn't overwrite it. 

if [ -z "$PS1" ]; then
# this extra check is to see if this command is interactive 
# if you print stuff during a non interactive session it can 
# break things like scp this is a slightly nuclear approach 
# to ignore the entire bashrc but it's also the safest. One 
# could go through and remove anything that prints to much
        : 
else
        if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
fi
