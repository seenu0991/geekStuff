
import dns.resolver
import csv 
import socket 
import sys
import os
import easygui
import whois

inputfile = easygui.fileopenbox(filetypes=['dns.txt'])

with open(inputfile, 'r') as ins:
    with open('ips.csv', 'w') as out:
        for host in ins.readlines():
            try:
                print('resolving:', host.strip())
                ip = socket.gethostbyname(host.strip())
                print('whois')
                dns = whois.whois(ip)
                out.write(f"{ip,host} registrar:{dns.registrar} updated_date:{dns.updated_date} created_date:{dns.creation_date} org:{dns.org} country:{dns.country}\n")
            except Exception as e:
                out.write(f'unable to resolve: {host.strip()}. Error: {e}')