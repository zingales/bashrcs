git config --global push.default upstream
git config --global core.excludesfile ~/.gitignore_global
git config --global branch.autosetupmerge true

#Git coloring
git config --global color.ui true
#---branch coloring
git config --global color.branch.current "magenta"
git config --global color.branch.local "yellow"
git config --global color.branch.remote "green"
#---diff coloring
git config --global color.diff.meta "white"
git config --global color.diff.frag "magenta bold"
git config --global color.diff.old "red bold"
git config --global color.diff.new "green bold"
git config --global color.diff.whitespace "white reverse"
#--- status coloring
git config --global color.status.added "green"
git config --global color.status.changed "yellow"
git config --global color.status.untracked "cyan"
git config --global color.status.branch "magenta"
