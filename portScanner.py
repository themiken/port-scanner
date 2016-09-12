#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Author: Mike16

import socket 
import os

BLAKC = "\033[1;30;40m"
RED = "\033[1;31;40m"
GREEN = "\033[1;32;40m"
YELLOW = "\033[1;33;40m" 
WHITE = "\033[1;37;40m"

ports = [21, 22, 23, 25, 42, 43, 53, 67, 79, 80, 102, 110, 115, 119, 123, 135, 137, 143, 161, 179, 379, 389, 443, 445, 465, 636, 993, 995, 1026, 1080, 1090, 1433, 1434, 1521, 1677,
           1701, 1720, 1723, 1900, 2409, 2082, 2095, 3101, 3306, 3389, 3390, 3535, 4321, 4664, 5190, 5500, 5631, 5632, 5900, 65535, 7070, 7100, 8000, 8080, 8880, 8799, 9100, 19430, 39720]


def connect(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        sock.close()
        return True
    except:
        return False


def scanPorts(web, ports):
    web = web.strip('http://')
    openPort = []
    closePort = []
    ip = socket.gethostbyname(web)
    print("HOST: " + web + " = " + ip)
    print("[*] Wait... (this could take a few minutes)")
    for x in ports:
        connection = connect(ip, x)
        if connection == True:
            openPort.append(x)
        else:
            closePort.append(x)
    showPorts(openPort, closePort)
    

def showPorts(openedPort, closedPort):
    for x in openedPort:
        print(GREEN + "OPEN: {0}".format(x))
    for y in closedPort:
        print(RED + "CLOSE: {0}".format(y))
    
    print(WHITE)




def main():
    os.system("cls")
    print(GREEN + "####################################")
    print("# -------- PORT SCANNER ---------- #")
    print(GREEN + "# -------- AUTOR:" + WHITE + " Mike16" + GREEN + " ----------#")
    print(GREEN + "####################################")
    print(RED + "[*] Enter the website")
    usrWeb = raw_input("--> " + WHITE)
    scanPorts(usrWeb, ports)

if __name__ == "__main__":
    main()
