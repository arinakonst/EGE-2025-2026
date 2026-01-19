from ipaddress import *
a = list(ip_network('172.16.160.0/255.255.240.0'))
res = 0
print(type(str(a[0])))
for x in list(ip_network('172.16.160.0/255.255.240.0')):
    x = list(map(int, str(x).split('.')))
    cou = 0
    for el in x:
        cou += bin(el).count('1')
    if cou %4 != 0:
        res += 1
print(res-2)   #3070
