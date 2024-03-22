#!/bin/python3
import sys #allow us to use command line arguments etc.
from datetime import datetime as dt
import socket
#Define our targets, make sure theres ip address input
if len(sys.argv) == 2: # this is as python3 scanner.py <ip>, <ip> is argument 1, 2 arguments to python 3      
    target = socket.gethostbyname(sys.argv[1]) #[1] selects ip, translates hostname to IP4   
else:
    print('Invalid amounts of arguments')
    print('Syntax error: Follow python3 scanner.py <ip> la')
    sys.exit()
#Add a pretty banner
print('-' *50)
print('Firing up, Scanning target ' + target )
print('Time started: ' + str(dt.now()))
print('-' * 50)
try:
    for port in range(50,85): # runs port from 50 - 85 cos its shitty
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is IPV4, SOCK_STREAM is your port   
        socket.setdefaulttimeout(1) #input is a float, detects port not open, then move on after 1s, if not it will hang forever!   
        result = s.connect_ex((target,port)) #if error connection, return error/if no error, returns 0
        print("Checking port {} right now".format(port))
        if result == 0:    # no error
            print("Port {} is open, noice.".format(port))
        s.close()
        
except KeyboardInterrupt: # use ctrl + c to exit program 
    print("\nExiting Program sua")
    sys.exit()
except socket.gaierror:
    print("Hostname cannot be resolved ¯\_(ツ)_/¯ ")
    sys.exit()
    
except socket.error:
    print("Couldnt connect to server ¯\_(ツ)_/¯ ")
    sys.exit()
