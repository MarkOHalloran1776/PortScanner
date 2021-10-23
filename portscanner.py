import socket
import re
import tkinter as tk
from tkinter import *

#Short port scanning script that prints out the port scanned and its service running if the port is indeed open, will eventually make a gui version for this
#DO NOT USE ON NETWORKS/ DEVICES YOU ARE UNAUTHORISED TO DO SO ON AS THIS MAY BE ILLEGAL

ip_add_format = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_format = re.compile("([0-9]+)-([0-9]+)")

ip_addr = input("Select IP address to port scan")
print(ip_addr)

if (ip_addr.format(ip_addr)):
    print("valid ip")
else:
    print("Invalid IP")


range_of_ports = input("Input the Range of Ports example ""1-10")

ports = range_of_ports.split("-")
start_port = int(ports[0])
end_port = int(ports[1])
ports_open = []

for port_num in range(start_port, end_port + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_in_use:
            socket_in_use.settimeout(0.5)
            socket_in_use.connect((ip_addr, port_num))
            ports_open.append(port_num)

    except:
        pass

for i in ports_open:
    serviceName = socket.getservbyport(i, "tcp")
    print(f"Port {serviceName}:{i} is open on {ip_addr}")
