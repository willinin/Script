import crypt
from passlib.hash import sha512_crypt

def testPass(cryptPass):
	salt = cryptPass[3:11]
	dictFile = open('dictionary.txt','r')
	for word in dictFile.readlines():
		cryptWord = word.strip('\n')
		cryptWord = sha512_crypt.encrypt(cryptWord, salt=salt, rounds=5000)
		if (cryptWord == cryptPass):
			print "[+] Found Password: "+word+"\n"
			return
	print "[-] Password Not Found.\n"
	return

def main():
	passFile = open('passwords.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Cracking Password For: "+user
			testPass(cryptPass)

if __name__ == "__main__":
	main()
