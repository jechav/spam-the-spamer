#!/bin/sh
#
# crontab -e run at 2am
# 0 2 * * * bash $HOME/echamor-app/scripts/daily_backup.sh >> $HOME/upload.log
#
#
cd $(dirname $0)

echo "Running global sura script"
# Run the global sura script
/root/.nvm/versions/node/v24.20.0/bin/npm run global-sura 3 10

echo "Global sura script completed"
