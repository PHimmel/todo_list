#!/bin/bash
cd ..
printf "alias todo=`$PWD + main`" >> ~/.bashrc
exec "$SHELL"

