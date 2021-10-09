#!/bin/sh

wget https://github.com/browsh-org/browsh/releases/download/v1.6.4/browsh_1.6.4_linux_amd64.deb

sudo dpkg -i ./browsh_1.6.4_linux_amd64.deb

sudo rm -r browsh_1.6.4_linux_amd64.deb

echo 'browsh installation complete.'
