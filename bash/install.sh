#!/bin/bash

localpath="$(pwd)"

# echo $localpath

zsh_installed() {
	grep -q '^export MYTILS_PATH=' ~/.zshrc && return 0 || return 1
}

install_zsh() {
	echo "Installing Sasha's utils"
	echo >> ~/.zshrc
        echo "# Sasha's utils" >> ~/.zshrc
        echo "export MYTILS_PATH=$localpath" >> ~/.zshrc
        echo 'export PATH="$MYTILS_PATH:$PATH"' >> ~/.zshrc
        echo >> ~/.zshrc
	
	echo "# Autocomplete " >> ~/.zshrc
	cat autocomplete_zsh.txt >> ~/.zshrc
	echo "# End sasha utils" >> ~/.zshrc
	echo >> ~/.zshrc
	# zsh -c "source ~/.zshrc"
}

backup_zsh() {
	echo "backing up ~/.zshrc"
	cp ~/.zshrc ~/.zshrc.mytils.bak
	echo "~/.zshrc backed up"
}

restore_zsh() {
	echo "restoring ~/.zshrc from backup"
	mv ~/.zshrc.mytils.bak ~/.zshrc
	echo "~/.zshrc restored"
}

if [ -f ~/.zshrc ]; then

	if zsh_installed; then
		echo "The utils have already been installed"
	else
		echo "Adding the scripts to the ZSH"
		backup_zsh
		install_zsh || restore_zsh
	fi
else
	echo ".zshrc not found"
fi

