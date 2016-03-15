# pingsweep
Lightweight IPv4 Pingsweeper - quickly ping many IP addresses

# Under Construction
I'm currently in the process of translating my currently existing 'bashping' code, written in bash, into python here.  The original pingsweep can be found at "https://github.com/sirpsycho/bashping".

# Current Update
The code is functional but still requires some bug fixes and additional features.  These include:
 - resolve subprocess KeyboardInterupt error on Ctrl-C exit
 - create check for fping install before executing
 - add ETA estimation functionality
 - customize help/usage text for -h option
 - add option to omit .0 and .255 addresses? idk
 - TESTING

In relationship to the bashping project on which this is based, this now includes a more functional way of creating the IP range.  This includes:
 - the ability to define starting and ending IPs down to the last octet (bashping would always ping from 0 to 255 on the last octet)
 - the ability to ping up to a full A-block (16.8 million IPs) in a single command execution
 - if only one IP is supplied, it will only ping that ip, unless the last octet is a '0', in which case it will ping the whole /24
