#encoding:utf-8
import optparse
import nmap

def nmapScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print "[*] "+ tgtHost + " tcp/" +tgtPort +" "+state

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
    if (tgtHost == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
    main()
