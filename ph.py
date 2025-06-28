
import urllib.error
from lxml import html
import re
#import requests
import urllib.request 
f = open("ph_input.txt", "r",encoding="utf-8")
n = 0 
with open("ph.m3u", 'w',encoding="utf-8") as file_o:
    file_o.write(r'')
    
for line in f:
    n = n+1
    if not line.startswith('#'):
        print("\nprocessing: line "+str(n)+": "+str(line))
        if(line.strip()==""):
            continue
        try:
            data = urllib.request.urlopen(line)
            tree = html.fromstring(data.read()) 
            item = tree.xpath(r'//*[@id="player"]/script[1]/text()')
            title = tree.xpath(r'//h1/span')[0].text
        except urllib.error.HTTPError as e:
            print(e)
            continue
        except Exception as e2:
            print ("Error",e2)
            continue
        #/html/body/div[5]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/script[1]/text()
        #//*[@id="player"]/script[1]/text()
        #//*[@id="hd-leftColVideoPage"]/div[1]/div[4]/h1/span
        #title = tree.xpath(r'//*[@id="videoTitle"]/span')[0].text
        if(len(item)>0):
            res = item[0]
            #print(res)
            p = r'"videoUrl":"(.*?)"'
            #p = r'"mediaDefinitions":\[(.*?)\]'
            links = re.findall(p,res)
            if(len(links)>0):
                #link = links[0]
                highres=0
                l = ""
                
                for link in reversed(links):
                    #print(link+"\n")
                    #m = re.match(r'.*?\D(\d+)P_\d+K.*',link)
                    m = re.match(r'.*?\D(\d+)P_\d+K.*',link)
                    #print("$$"+link)
                    #m = re.match(r'.*?(?<=\/)(\d+)P_\d+K.*',link)
                    if m:
                        #print(m.group(1))
                        newres = int(m.group(1))
                        if newres>highres:
                            highres = newres
                            l = link.replace('\\','')
                            with open("ph.m3u", 'a',encoding="utf-8") as file_o:
                                file_o.write(r'#EXTINF:-1 group-title="ph",'+title+"\n")
                                file_o.write(l+"\n")
                            
                            #with open("input_ph_bkp.txt", 'a',encoding="utf-8") as file_o:
                            #   file_o.write(line)
                            
                print("final: "+l)
        
f.close()
#f = open("input_ph.txt", "w")
#f.close()
