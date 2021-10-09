#!/bin/sh

wget ftp://ftp.invisible-island.net/lynx/tarballs/lynx2.8.9rel.1.tar.gz

tar -xzf lynx2.8.9rel.1.tar.gz

cd lynx2.8.9rel.1.tar.gz/

./configure

make

sudo make install
