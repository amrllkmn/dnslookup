# dnslookup
## Description
The coursework tasked students to find IP addresses, and then map out the routes taken to access that particular IP address.

### dnslookup.c
It returns the IPv4 and IPv6 addresses of the website.

```sh
bash-4.2$ ./dnslookup www.google.com
www.google.com IPv6 2a00:1450:4009:802::2004
www.google.com IPv4 216.58.198.100
```
### ip.py
Runs traceroute given a .txt file.

```sh
bash-4.2$ python ip.py google.txt
running traceroute IPv4 address...
running traceroute IPv6 address...
```

### script.sh
It runs the dnslookup, runs ip.py and outputs them to a .txt file.

```sh
bash-4.2$ ./script.sh
www.google.com
google.txt
running traceroute IPv4 address...
running traceroute IPv6 address...
```
### pro_ip.py
Processes the traceroute so that the output becomes  
from this:
```sh
traceroute to 216.58.198.100 (216.58.198.100), 30 hops max, 60 byte packets
 1  130.209.240.48  0.264 ms
 2  130.209.2.17  0.291 ms
 3  130.209.2.114  0.590 ms
 4  146.97.154.1  0.581 ms
 5  146.97.38.25  1.099 ms
 6  146.97.33.53  5.193 ms
 7  146.97.33.41  7.207 ms
 8  146.97.33.21  11.224 ms
 9  146.97.33.1  11.483 ms
10  72.14.217.18  11.155 ms
11  *
12  216.239.63.138  12.232 ms
13  74.125.242.115  12.137 ms
14  216.239.58.131  12.881 ms
15  216.239.58.178  12.399 ms
16  108.170.246.129  12.257 ms
17  64.233.175.155  11.774 ms
18  *
19  *
20  *
21  *
22  *
23  *
24  *
25  *
26  *
27  *
28  *
29  *
30  *
``` 
to this:
```sh
"130.209.240.48" -- "130.209.2.17"
"130.209.2.17" -- "130.209.2.114"
"130.209.2.114" -- "146.97.154.1"
"146.97.154.1" -- "146.97.38.25"
"146.97.38.25" -- "146.97.33.53"
"146.97.33.53" -- "146.97.33.41"
"146.97.33.41" -- "146.97.33.21"
"146.97.33.21" -- "146.97.33.1"
"146.97.33.1" -- "72.14.217.18"
"72.14.217.18" -- "216.239.63.138"
"216.239.63.138" -- "74.125.242.115"
"74.125.242.115" -- "216.239.58.131"
"216.239.58.131" -- "216.239.58.178"
"216.239.58.178" -- "108.170.246.129"
"108.170.246.129" -- "64.233.175.155"
```
