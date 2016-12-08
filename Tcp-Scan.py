#encoding:utf-8
import optparse
import socket
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost,tgtPort):
    try:
        connSkt=socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('I just want to know your opening ports\n')
        results=connSkt.recv(1024)
        screenLock.acquire()
        print '[+] %d/tcp open' %tgtPort
        print '[+] ' + str(results)
    except:
        screenLock.acquire()
        print '[-] %d/tcp closed' %tgtPort
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s':Unknown host " %tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for :' +tgtName[0]
    except:
        print '\n[+] Scan Results for :' +tgtIP
    setdefaulttimeout(10)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan,args=(tgtHost,int(tgtPort)), kwargs=None, verbose=None)
        t.start()

def main():
    parser = optparse.OptionParser("%prog" + "-H <target Host> -p <target port> and " + "default scan-port is 80")
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-p',dest='tgtPort',type='string',default='80,443',help='specify target port[s] separated by comma')
    (options,args)=parser.parse_args()
    tgtHost=options.tgtHost
    tgtPorts=str(options.tgtPort).split(',')
    if(tgtHost == None):
        print '[-] You must specify a target host.'
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
