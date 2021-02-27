#!/usr/bin/env bash
find $1 -type f -name *.c -o -name *.h | grep -v '\.svn' | xargs cat | sed '/^\s*$/d' | wc -l
