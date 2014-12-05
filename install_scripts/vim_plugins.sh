#git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
ensure_git ~/.vim/bundle/Vundle.vim https://github.com/gmarik/Vundle.vim.git
#install all vim plugins
vim +PluginInstall +qall

#####specific vim plugin requirements
#command t
cd ~/.vim/bundle/command-t/ruby/command-t
ruby extconf.rb && make && echo "Command-t Installed"
#you complete me
cd ~/.vim/bundle/YouCompleteMe/
./install.sh --clang-completer && echo "YouCompleteMe Installed"
