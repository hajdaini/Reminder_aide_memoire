#!/bin/bash

sudo  apt-get update -y

install_zsh(){
    apt-get install -y zsh
    chsh --shell /bin/zsh
    /bin/zsh
    printf("Logout/Login to see your zsh as your default interperter")
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
    printf("vim ~/.p10k.zs \n to enabla CPU/ram/disk_usage")
}

install_zsh
