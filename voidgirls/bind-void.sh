# Set up a default .bashrc script and alias grungegirl to it.

sudo cp /etc/skel/.bashrc ~/.bashrc
echo "alias grungegirl='python ~/.grungegirl/voidgirls/voidgirls.py'" >> ~/.bashrc

echo 'インストールが完了.'
echo 'version 0.4 - huntress'

. ~/.bashrc
