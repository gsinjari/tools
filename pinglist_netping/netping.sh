#!/bin/bash
# author      : @g0vandS, Govand Sinjari
# license           : MIT
# netping
# By Govand - 2013-06-26
#!/bin/bash
for ips in $(seq 1 254); do
	ping 192.168.0.$ips -c 1 | grep "bytes from" &
done