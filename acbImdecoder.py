import re;
import urllib.request;
import AdFlyDecoder as  adf;

links = ['http://adf.acb.im/33',
'http://adf.acb.im/A6',
         'http://adf.acb.im/MW',
         'http://adf.acb.im/QH',
         'http://adf.acb.im/WD'];
for link in links:
    x = urllib.request.urlopen(link).read();
    r = r'ysmm.*?=(.*?);';
    ysmm = re.findall(r,str(x));

    ysmmFinal = ysmm[0].strip().replace('\\\'', '');
    #print(ysmmFinal);
    adf.acbImLinkMod(ysmmFinal);
