#!/bin/bash
printf "running installer\n"
cd ..
echo "alias todo=`$PWD + main`" >> ~/.bashrc
exec "$SHELL"
printf "installed\n"

