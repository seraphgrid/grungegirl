#!/bin/bash

if [ ! -f "~/.bashrc_bak/.bashrc"]; then
  sudo cp ~/.bashrc_bak/.bashrc ~
  sudo rm -r ~/.bashrc_bak
fi

if [ ! -f "~/.grungegirl/" ]; then
 sudo rm -r ~/.grungegirl
fi
