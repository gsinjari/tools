#!/bin/bash
# author      : @g0vandS, Govand Sinjari
# license           : MIT
# PingList Nr IP1 IP2 IP3 IP4
# By Govand - 2013-06-26
for ((x=2; x<=$# ;x++)); do
    eval ipx=\$$x
    #ping $ipx -c $1 | grep "bytes from" | cut -d" " -f4 | cut -d":" -f1 &
    ping $ipx -c $1 | grep "bytes from" &
done
