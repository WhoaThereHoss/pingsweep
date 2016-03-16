#!/usr/bin/python

### IPv4 Pingsweeper (Class B)
### 
### 

## Imports

import time
import optparse
import sys
import subprocess


## Define functions

def validate_ip(ip):
    a = ip.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def parse_ip(ip):
    a = ip.split('.')
    return a

def make_ip_list(ipBeg, ipEnd):
    
    ip_list = []
    start = list(map(int, ipBeg.split(".")))
    end = list(map(int, ipEnd.split(".")))
    
    if ipBeg == ipEnd:
        if start[3] == 0:
            end[3] = 255
    
    if (end[0] == start[0] and end[1] > start[1]) or (end[0] == start[0] and end[1] == start[1] and end[2] > start[2]) or (end[0] == start[0] and end[1] == start[1] and end[2] == start[2] and end[3] >= start[3]):
        temp = start

        ip_list.append(ipBeg)
        while temp != end:
            start[3] += 1
            for i in (3, 2, 1):
                if temp[i] == 256:
                    temp[i] = 0
                    temp[i-1] += 1
            ip_list.append(".".join(map(str, temp)))

        return ip_list
    else:
        print "Error - The second IP must be greater than or equal to the first IP."
        print "'-h' option for help menu"
        sys.exit()

def make_grep_string(v, r, d):
    grep_string = ""
    if d:
        return grep_string
    elif v:
        if r:
            grep_string = " 2>&1 | grep -F -v '1/1/0%'"
        else:
            grep_string = " 2>&1 | grep -F -v '1/0/100%'"
    else:
        if r:
            grep_string = " 2>&1 | grep '1/0/100%' | cut -f1 -d' '"
        else:
            grep_string = " 2>&1 | grep '1/1/0%' | cut -f1 -d' '"
    return grep_string


## Get Options

parser = optparse.OptionParser()

parser.add_option('-v', '--verbose',
                  dest="verbose",
                  default=False,
                  action="store_true",
                  help='include fping statistics for each ping',
                 )
parser.add_option('-r', '--reverse',
                  dest="reverse",
                  default=False,
                  action="store_true",
                  help='display failed pings instead of successful pings',
                 )
parser.add_option('-t', '--timeout',
                  dest="timeout",
                  default=200,
                  help='define a ping timeout in miliseconds (default is 200)',
                 )
parser.add_option('-d', '--debug',
                  dest="debug",
                  default=False,
                  action="store_true",
                  help='display all pings, failed and successful',
                 )

options, remainder = parser.parse_args()


## Initialize variables

verbose = options.verbose
reverse = options.reverse
timeout = options.timeout
debug = options.debug
ipBeg = "none"
ipEnd = "none"
single = False



if len(remainder) == 1:
    if validate_ip(remainder[0]):
        single = True
        ipBeg = remainder[0]
    else:
        print "Invalid IP Address '%s'" % (remainder[0])
        print "'-h' option for help menu"
        sys.exit()
elif len(remainder) == 2:
    if validate_ip(remainder[0]):
        ipBeg = remainder[0]
    else:
        print "Invalid IP Address '%s'" % (remainder[0])
        print "'-h' option for help menu"
        sys.exit()
    if validate_ip(remainder[1]):
        ipEnd = remainder[1]
    else:
        print "Invalid IP Address '%s'" % (remainder[1])
        print "'-h' option for help menu"
        sys.exit()
else:
    print "Invalid arguments. Use -h option for usage format."
    sys.exit()
    
if single:
    ipEnd = ipBeg

ip_list = make_ip_list(ipBeg, ipEnd)

print "Starting ping sweep on %s through %s...\n" % (ip_list[0], ip_list[-1])
    
if verbose:
    print "[+] Verbose option set\n"

if timeout != 200:
    print "[+] Timeout set to %s milliseconds\n" % (timeout)

if reverse:
    print "[+] Reverse option set - displaying failed pings\n"

if debug:
    print "[+] Debug option set - displaying all pings\n"

print "Scan start: %s\n......" % (time.ctime())

grep_string = ""
for ip in ip_list:
    bash_string = "fping -a -c1 -t%s %s%s" % (timeout, ip, make_grep_string(verbose, reverse, debug))
    subprocess.call(bash_string, shell=True)

print "......\nScan finished at: %s" % (time.ctime())