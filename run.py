import dns.resolver
import csv 
import socket 
import sys
import os
import easygui


inputfile = easygui.fileopenbox(filetypes=['dns.txt'])
with open(inputfile, 'r') as ins:
    with open('ip.txt','a') as out:
        for dns in ins.readlines():
            #dns = dns.stirp()
            try:
                print('resolving:'+dns)
                ip = socket.gethostbyname(dns)
                out.write(dns + '-' + ip + '\n')
            except:
                print('unable to resolve:' + dns)

#dm_fin = whois.whois('ballade.real.notaires.com')
#print(dm_fin)
