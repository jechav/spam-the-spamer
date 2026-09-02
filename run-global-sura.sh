#!/bin/sh
# every 1 hour 
# 0 * * * * bash run-global-sura.sh >> /var/log/run-global-sura.log 2>&1
#

cd $(dirname $0)

# Explicitly add the NVM node binary folder to the PATH
export PATH="/root/.nvm/versions/node/v24.20.0/bin:$PATH"

echo "Running global sura script"
echo "Current directory: $(pwd)"

TIMES_RUN=$((RANDOM % 3 + 3)) # Between 3 and 5 times
echo "Times to run: $TIMES_RUN"
SLEEP_TIME=$((RANDOM % 21 + 20)) # Between 20 and 40 seconds
echo "Sleep time between runs: $SLEEP_TIME seconds"

# Now you can use standard command names safely
NPM_VERSION=$(npm --version)
echo "NPM version: $NPM_VERSION"


# Run the global sura script
for i in $(seq 1 $TIMES_RUN); do
  sleep $SLEEP_TIME
  echo "Running global sura iteration $i"
  DELAY_TIME=$((RANDOM % 3 + 1)) # Between 1 and 3 seconds
  npm run global-sura $DELAY_TIME 120
done

current_time=$(date "+%Y-%m-%d %H:%M:%S")
echo "Global sura script completed at $current_time"

