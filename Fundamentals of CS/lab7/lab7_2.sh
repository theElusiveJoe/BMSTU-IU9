#!/usr/bin/env bash

counter=0
for file in $(find $1 -name '*.c' -o -name '*.h'); do
      echo ${file}:
      cat $file
      let "counter = $counter + $(cat $file| sed /^\s*$/d | wc -l)"
done
echo -e "\n counter = $counter"
