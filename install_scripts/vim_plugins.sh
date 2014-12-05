#git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
ensure_git ~/.vim/bundle/Vundle.vim https://github.com/gmarik/Vundle.vim.git

#install all vim plugins
vim +PluginInstall +qall
if [ $? -eq 0 ]; then
  #####specific vim plugin requirements
  #this doesn't check if these things have been run yet
  #command t
  COMMAND_T_DIR=~/.vim/bundle/command-t/ruby/command-t 
  if [ -d $COMMAND_T_DIR ]; then
    cd $COMMAND_T_DIR
    ruby extconf.rb && make && echo "---- Command-t Installed"
  fi;

  #you complete me
  YOUCOMPELETEME_DIR=~/.vim/bundle/YouCompleteMe
  if [ -d $YOUCOMPELETEME_DIR ]; then
    cd $YOUCOMPELETEME_DIR
    #currently reinstalls everytime which is rather annoying
    #./install.sh --clang-completer && echo "----YouCompleteMe Installed"
  fi;
fi;
