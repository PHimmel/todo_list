#!/bin/bash
# change the locale to /bin
echo "running installer"
cd ..
printf "alias todo=`$PWD + main`" >> ~/.bashrc
exec "$SHELL"
echo "installed"

