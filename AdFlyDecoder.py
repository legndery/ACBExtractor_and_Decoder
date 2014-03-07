import base64;
from tkinter import Tk
def acbImLink(sc):
        c = str('');
        h=str('');
        x=0;
        print("Open jDownloader. The url will be copied to clipboard");
        security_code = sc;
        for i in security_code:
                if x%2==0:
                        c = c+str(i);
                else:
                        h=str(i)+h;
                x+=1;

        new_code = c+h;
        url = base64.b64decode(new_code);
        print(url[2:]);
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(url[2:])
        r.destroy()
        input();

if __name__== "__main__":
        security_code = input("ysmm=");  
        acbImLink(security_code);

        
def acbImLinkMod(sc):
        c = str('');
        h=str('');
        x=0;
        security_code = sc;
        for i in security_code:
                if x%2==0:
                        c = c+str(i);
                else:
                        h=str(i)+h;
                x+=1;

        new_code = c+h;
        url = base64.b64decode(new_code);
        with open('Files.txt', 'a') as file:
                file.write(str(url[2:])+'\n');
        print(url[2:]);
