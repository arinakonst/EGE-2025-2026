from ipaddress import *
net = ip_network('212.192.32.96/255.255.255.224')
for ip in net:
    s = bin(int(ip))[2::]
    if '111' not in s[24::] and '000' not in s[24::]:
        print(s[24::])
