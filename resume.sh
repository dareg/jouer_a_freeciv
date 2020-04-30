#!/bin/sh

# $1 is the savegame to load 
/usr/games/freeciv-server --Database fc_auth.conf --auth -d 3 -l server.log -s saves -r cmd -f $1

