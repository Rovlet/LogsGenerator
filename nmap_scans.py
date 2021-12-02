import sys
import os
from settings import *
import nmap  # import nmap.py module


nm = nmap.PortScanner()  # instantiate nmap.PortScanner object

nm.scan(VICTIM_IP, '22-443')  # scan host 127.0.0.1, ports from 22 to 443
nm.command_line()  # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
nm.scaninfo()  # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
nm.all_hosts()  # get all hosts that were scanned
nm[VICTIM_IP].hostname()  # get one hostname for host 127.0.0.1, usualy the user record
nm[VICTIM_IP].hostnames()  # get list of hostnames for host 127.0.0.1 as a list of dict [{'name':'hostname1', 'type':'PTR'}, {'name':'hostname2', 'type':'user'}]
nm[VICTIM_IP].state()  # get state of host 127.0.0.1 (up|down|unknown|skipped)
nm[VICTIM_IP].all_protocols()  # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
if ('tcp' in nm[VICTIM_IP]):
    list(nm[VICTIM_IP]['tcp'].keys())  # get all ports for tcp protocol

nm[VICTIM_IP].all_tcp()  # get all ports for tcp protocol (sorted version)
nm[VICTIM_IP].all_udp()  # get all ports for udp protocol (sorted version)
nm[VICTIM_IP].all_ip()  # get all ports for ip protocol (sorted version)
nm[VICTIM_IP].all_sctp()  # get all ports for sctp protocol (sorted version)
if nm[VICTIM_IP].has_tcp(22):  # is there any information for port 22/tcp on host 127.0.0.1
    nm[VICTIM_IP]['tcp'][22]  # get infos about port 22 in tcp on host 127.0.0.1
    nm[VICTIM_IP].tcp(22)  # get infos about port 22 in tcp on host 127.0.0.1
    nm[VICTIM_IP]['tcp'][22]['state']  # get state of port 22/tcp on host 127.0.0.1 (open

# a more usefull example :
for host in nm.all_hosts():
    print('Host : {0} ({1})'.format(host, nm[host].hostname()))
    print('State : {0}'.format(nm[host].state()))

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}'.format(proto))

        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))

print(nm.csv())
# If you want to do a pingsweep on network 192.168.1.0/24:
nm.scan(hosts=VICTIM_NETWORK, arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))

nma = nmap.PortScannerAsync()


def callback_result(host, scan_result):
    print(host, scan_result)


nma.scan(hosts=VICTIM_NETWORK, arguments='-sP', callback=callback_result)

while nma.still_scanning():
    print("Waiting ...")
    nma.wait(2)

if (os.getuid() == 0):
    print('----------------------------------------------------')
    # Os detection (need root privileges)
    nm.scan(VICTIM_IP, arguments="-O")
    if 'osmatch' in nm[VICTIM_IP]:
        for osmatch in nm[VICTIM_IP]['osmatch']:
            print('OsMatch.name : {0}'.format(osmatch['name']))
            print('OsMatch.accuracy : {0}'.format(osmatch['accuracy']))
            print('OsMatch.line : {0}'.format(osmatch['line']))
            print('')

            if 'osclass' in osmatch:
                for osclass in osmatch['osclass']:
                    print('OsClass.type : {0}'.format(osclass['type']))
                    print('OsClass.vendor : {0}'.format(osclass['vendor']))
                    print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
                    print('OsClass.osgen : {0}'.format(osclass['osgen']))
                    print('OsClass.accuracy : {0}'.format(osclass['accuracy']))
                    print('')

    if 'fingerprint' in nm[VICTIM_IP]:
        print('Fingerprint : {0}'.format(nm[VICTIM_IP]['fingerprint']))

    # Vendor list for MAC address
    print('scanning localnet')
    nm.scan(VICTIM_NETWORK, arguments='-O')
    for h in nm.all_hosts():
        print(h)
        if 'mac' in nm[h]['addresses']:
            print(nm[h]['addresses'], nm[h]['vendor'])

# Read output captured to a file
# Example : nmap -oX - -p 22-443 -sV 127.0.0.1 > nmap_output.xml

with open("./nmap_output.xml", "r") as fd:
    content = fd.read()
    nm.analyse_nmap_xml_scan(content)
    print(nm.csv())

# Progressive scan with generator
nm = nmap.PortScannerYield()
for progressive_result in nm.scan(VICTIM_NETWORK, '22-25'):
    print(progressive_result)
