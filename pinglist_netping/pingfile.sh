#!/bin/bash
# author      : @g0vandS, Govand Sinjari
# license           : MIT
# pingfile nr file.txt
# By Govand - 2015-04-04
for ip in $(cat $2); do
 	 ping $ip -c $1 | grep "bytes from" &
done
