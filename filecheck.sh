#!/bin/sh

if [ ! -f "$HOME/.bashrc_bak" ]; then
  sudo mv -r ~/.bashrc_bak ~/.bashrc
  sudo rm -r ~/.bashrc_bak
fi

if [ ! -f "$HOME/.grungegirl/" ]; then
 sudo rm -r ~/.grungegirl
fi
