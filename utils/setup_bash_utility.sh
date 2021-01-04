#!/bin/bash
echo running installer
cd ..
printf "alias todo=`$PWD + main`" >> ~/.bashrc
exec "$SHELL"
echo installed

