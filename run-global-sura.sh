#!/bin/sh
# every 1 hour 
# 0 * * * * bash run-global-sura.sh >> /var/log/run-global-sura.log 2>&1
#

cd $(dirname $0)

# Explicitly add the NVM node binary folder to the PATH
export PATH="/root/.nvm/versions/node/v24.20.0/bin:$PATH"

echo "Running global sura script"
echo "Current directory: $(pwd)"


# Now you can use standard command names safely
NPM_VERSION=$(npm --version)
echo "NPM version: $NPM_VERSION"


# Run the global sura script
npm run global-sura 3 10

current_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "Global sura script completed at $current_time"
