import subprocess
import sys
files = sys.argv[1]
file = open(files,"r")
ipaddr = []
i = 0
j = 0
for line in file:
    ipaddr.append(line.split(" ",1)[1])

for ip in ipaddr:
    type = files[0:-4]
    addr = ip[5:-1]
    if ip[3]=="4":
        x = open(type+"ipv4"+"-" + str(i) +".txt","w")
        print "running traceroute on IPv4 address..."
        subprocess.Popen(["traceroute","-4", "-q 1","-n", addr],stdout=x)
    #    print ip_elt[0]
        x.close()
        int(i)
        i=i+1

    elif ip[3]=="6":
        y = open(type +"ipv6"+"-"+ str(j) +".txt","w")
        print "running traceroute on IPv6 address..."
        subprocess.Popen(["traceroute","-6", "-q 1","-n", addr],stdout=y)
        y.close()
        int(j)
        j=j+1
    else:
        print file.readline()

file.close()
