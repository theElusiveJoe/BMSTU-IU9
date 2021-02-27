#!/usr/bin/env bash

rm *.txt #для удобства

while true; do
      if jobs | grep 'Running' > /dev/null; then
            echo -e "already running \ni will sleep for $2 secs\n"
            sleep $2
      else
            name=$(date +"%T")
            echo -e "***********\nstarted process $(date +"%T")\n***********\n"
            $1 > "${name}.txt" 2 > "${name}_errors.txt" &
      fi
done
