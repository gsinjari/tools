#!/bin/bash
# author      : @g0vandS, Govand Sinjari
# license           : MIT
# netpingplus 10 10 10 1
# By Govand - 2013-06-26

if [ -z ""$1"" ]; then a=192; else a=$1; fi
if [ -z ""$2"" ]; then b=168; else b=$2; fi
if [ -z ""$3"" ]; then c=0; else c=$3; fi
if [ -z ""$4"" ]; then d=1; else d=$4; fi
for z in $(seq $a 255); do
  for y in $(seq $b 255); do
    for x in $(seq $c 255); do
      echo "pinging subnet $z.$y.$x.0"
      for w in $(seq $d 254); do
        ping $z.$y.$x.$w -c 1 | grep "bytes from" | cut -d" " -f4 | cut -d":" -f1 &
      done
    done
  done
done