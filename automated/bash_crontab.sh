#!/bin/sh
#
# crontab -e run at 2am
# */5 * * * * bash $HOME/span-the-spamer/automated/bash_crontab.sh >> $HOME/automated.log
#
#
cd $(dirname $0)

npm run cy:run
