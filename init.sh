#!/bin/sh

conffile="fc_auth.conf"
touch $conffile
echo '[fcdb]' >> $conffile
echo 'backend="sqlite"' >> $conffile
echo 'database="freeciv.sqlite"' >> $conffile

/usr/games/freeciv-server --Database fc_auth.conf --auth --Newusers -l server.log -s saves -r cmd

