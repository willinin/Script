#encoding:utf-8
import crypt
def testPass(cryptPass):
    salt=cryptPass[0:2]
    dictFile=open('dictionary.txt','r')
    for word in dictionary.readlines():
        word=word.strip('\n')
        crtptword=crypt.crypt(word, salt)
        if(cryptPass==crtptword):
            print "[+] Found Password:"+word+"\n"
            return
    print "[-] Password Not Found.\n"
    return

def main():
    passFile=open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user=line.split(':')[0]
            cryptPass=line.split(':')[1].strip(' ')
            print "[*] Cracking Password For :"+user
            testPass(cryptPass)

if __name__=="__main__":
    main()
