# This program generates Download links to each and every video in any Lynda.com Course
# It will use your browser cookie, so you to be logged in with your Lynda account, in chrome browser, before running this program
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import browsercookie
import json

#grabbing cookie and requesting the provided lynda url
cj =browsercookie.chrome()

print("Lynda Course Downloader")
print("Just provide the link to any video in course and I'll give to links to all the videos in the course")
url=raw_input('Enter the URL to any video in Lynda course : ')
courseName = raw_input('Enter the Lynda course Name : ')
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
source_code = requests.get(url, headers=headers, timeout=10,cookies=cj)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"html.parser")


#finding links to all videos in given course
others = soup.find('div',{'id':'toc-content'})
others = others.findAll('a',{'class':'video-name'})
links = []
for a in others:
    links.append(a["href"])

f = open(courseName+" - Names.txt", "w+")
for i in range(len(links)):
    print(links[i])
    f.write(str(i+1)+": "+str(links[i])+"\n")
f.close()
    

for i in range(0,len(links)):
    url=links[i]
    source_code = requests.get(url, headers=headers, timeout=20,cookies=cj)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")

    video = soup.find('div',{'id':'courseplayer'})
    video = video.find('video',{'class':'player'})
    link = video["data-src"]
    print str(i+1)+"/"+str(len(links))+"----------"+str(((i+1)*100)/len(links))+"%"
    print str(link)
    f = open(courseName+" - Videos.txt","a+")
    f.write(str(link)+"\n")
    f.close()
    
