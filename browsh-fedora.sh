#!/bin/sh

wget https://github.com/browsh-org/browsh/releases/download/v1.6.4/browsh_1.6.4_linux_amd64.rpm

sudo rpm -i browsh_1.6.4_linux_amd64.rpm

rm -r browsh_1.6.4_linux_amd64.rpm

echo 'fedora installation complete or automatically skipped.'
