
from lxml import html
import re
#import requests
import urllib.request 
from urllib.request import urlopen, Request
with open("xh.m3u", 'w') as file_o:
    file_o.write(r'#EXTM3U ***selected XH medias***')
f = open("input_xh.txt", "r")
index = 0
for line in f:
    print("processing"+str(line))
    if(line.strip()==""):
        continue
    #headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    #reg_url = r'https://xhamster.com/videos/cory-chase-xh4wieL'
    #reg_url = r'https://xhamster.com/videos/oh-yeah-stepdaddy-fuck-me-while-no-one-sees-xhyhNvv'
    reg_url = line
    req = Request(url=reg_url,headers=headers)
    h = urlopen(req).read()
    #data = urllib.request.urlopen(line)
    #tree = html.fromstring(data.read()) 
    tree = html.fromstring(h) 
    #/html/head/link[27]

    #/html/head/link[27]
    items = tree.xpath(r'/html/head/link')
    #item = tree.xpath(r'//*[@id="player"]/script[1]/text()')
    #title = tree.xpath(r'//*[@id="videoTitle"]/span')[0].text
    title = tree.xpath(r'//title')[0].text
    index += 1
    for i in items:
        
        l= i.attrib['href']
        if l.endswith("m3u8"):
            print("link: "+l+"\n")
            with open("xh.m3u", 'a') as file_o:
                file_o.write(r'#EXTINF:-1 #EXTINF:-1  group-title="xh",'+str(index*2+1)+":"+title.replace('| xHamster','')+"\n")
                file_o.write(l+"\n")                       
        
f.close()

