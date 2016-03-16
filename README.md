# pingsweep
Lightweight IPv4 Pingsweeper - quickly ping many IP addresses

# Description

This utility is meant to quickly ping a large group of IP's.  Currently, in one command execution, this script can ping sweep up to one IPV4 A-block (x.x.x.x/8).

# Requirements

- BASH
- python
- fping

(should work on most linux distro's by default - may need to install fping)


# Usage

./pingsweep.py [options] start-ip end-ip

=============================

Example: "./pingsweep.py -t 150 10.0.0.0 10.0.5.255"

Result: pings all hosts from "10.0.0.0" through "10.0.5.255" (inclucive) with a ping timeout of 150 miliseconds

=============================

Example: "./pingsweep.py 192.168.1.0"

Result: pings all 256 IP's from 192.168.1.0 to 1922.168.1.255


# Under Construction
I'm currently in the process of translating my currently existing 'bashping' code, written in bash, into python here.  The original pingsweep can be found at "https://github.com/sirpsycho/bashping".

# Current Update
The code is functional but still requires some bug fixes and additional features.  These include:
 - create check for fping install before executing
 - add ETA estimation functionality
 - customize help/usage text for -h option
 - add option to omit .0 and .255 addresses? idk
 - TESTING

Fixes:
 - resolved subprocess KeyboardInterupt error on Ctrl-C exit
 - added timestamp and "last IP scanned" on Ctrl-C exit

In relationship to the bashping project on which this is based, this now includes a more functional way of creating the IP range.  This includes:
 - the ability to define starting and ending IPs down to the last octet (bashping would always ping from 0 to 255 on the last octet)
 - the ability to ping up to a full A-block (16.8 million IPs) in a single command execution
 - if only one IP is supplied, it will only ping that ip, unless the last octet is a '0', in which case it will ping the whole /24
