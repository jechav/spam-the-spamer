#!/bin/sh
#

cd $(dirname $0)

echo "Running global sura script"
echo "Current directory: $(pwd)"


# get npm path
NPM_VERSION=$(/root/.nvm/versions/node/v24.20.0/bin/npm --version)
echo "NPM version: $NPM_VERSION"


# Run the global sura script and get the output
/root/.nvm/versions/node/v24.20.0/bin/npm run global-sura 3 10

current_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "Global sura script completed at $current_time"
