from pexpect import pxssh
def send_command(s,cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before

def connect(host,user,password):
    try:
        s=pxssh.pxssh()
        s.login(host,user,password)
        return s
    except:
        print "[-] Error Connecting"
        exit(0)

def main():
    s=connect('127.0.0.1','root','190050')
    send_command(s,'cat /etc/shadow |grep root')

if __name__=="__main__":
    main()
