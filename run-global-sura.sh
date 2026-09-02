#!/bin/sh
#
# crontab -e run at 2am
# 0 2 * * * bash $HOME/echamor-app/scripts/daily_backup.sh >> $HOME/upload.log
#
#
cd $(dirname $0)

echo "Running global sura script"
echo "Current directory: $(pwd)"

# get npm path
NPM_PATH=$(which npm)
echo "NPM path: $NPM_PATH"

# Run the global sura script and get the output
npm run global-sura 3 10 >> $HOME/global-sura.log 2>&1

echo "Global sura script completed"
