# pingsweep
Lightweight IPv4 Pingsweeper - quickly ping many IP addresses

# Description

This utility provides a simple interface allowing a user to quickly ping a large group of IP's.

============================================

 - begin enumeration on unknown networks
 - check connectivity of a list of networked devices
 - define a custom ping timeout for faster or more thorough scans
 - ping up to one full IPv4 A-block (x.x.x.x/8)
 - default output is in a list-friendly format

# Requirements

- BASH
- python
- fping

(should work on most linux distro's by default - may need to install fping)


# Usage

./pingsweep.py [options] start-ip end-ip

=============================

Ping a range: `./pingsweep.py 10.0.0.0 10.0.5.255`



Ping a list: `./pingsweep.py -l IP_list.txt`



Ping a /24 C-block: `./pingsweep.py 192.168.1.0`


# Current Update
Ideas for improvement:
 - add ETA estimation functionality
 - implement ability to handle IP's in CIDR notation

Recent fixes and added functionality:
 - added '-l' option to enter a text file list of IP's to ping
 - customized help/usage text for -h option
 - created check for fping install before executing
 - added timestamp and "last IP scanned" on Ctrl-C exit
