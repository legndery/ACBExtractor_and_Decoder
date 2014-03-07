import re
import urllib.request
def urlExtractor(url):
    i=1;
    data = urllib.request.urlopen(url).read();
    regx = r'<input class="button-auto" onclick="window.open\(\\\'(.+?)\\\'\);return false;"'
    listinit = re.findall(regx,str(data))
    listF = list();
    for item in listinit:
        if(item not in listF):
            listF.append(item);

    for item in listF:
        #print(i);
        print(item)
        i+=1;

if __name__=="__main__":
    url = input("Enter the Url:");
    urlExtractor(url);
