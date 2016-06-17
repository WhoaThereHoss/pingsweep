# pingsweep
Lightweight Pingsweeper - quickly ping many hosts

# Description

This utility provides a simple interface allowing a user to quickly ping a large group of hosts by IPv4 address or by hostname.

============================================

 - begin enumeration on unknown networks
 - check connectivity of a list of networked devices
 - define a custom ping timeout for faster or more thorough scans
 - ping up to one full IPv4 A-block (x.x.x.x/8)
 - default output is in a list-friendly format


# Usage

./pingsweep.py [options] start-ip end-ip

=============================

Ping a range: `./pingsweep.py 10.0.0.0 10.0.5.255`



Ping a list: `./pingsweep.py -l IP_list.txt`



Ping a /24 C-block: `./pingsweep.py 192.168.1.0`

=============================

```
./pingsweep.py -h
Usage: ./pingsweep.py [options] <start-ip> <end-ip>

Options:
  -h, --help                    show this help message and exit
  -v, --verbose                 include fping statistics for each ping
  -r, --reverse                 display failed pings instead of successful pings
  -t TIMEOUT, --timeout=TIMEOUT define a ping timeout in miliseconds (default is 200)
  -n, --hostnames               Attempt to resolve hostnames for successful pings
  -d, --debug                   display all pings, failed and successful
  -l IP_FILE, --list=IP_FILE    define a text file of one IP per line to ping
 ```
