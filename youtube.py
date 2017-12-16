import urllib2
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import requests
import os


def quote(query):
    ans = ""
    for i in range(len(query)):
        if query[i] == " ":
            ans += "+"
        else:
            ans += query[i]
    return ans


print "Welcome to Youtube Streamer.\nEnter your Query:"
query = raw_input()
query = quote(query)

url = "https://www.youtube.com/results?search_query=" + query

    # add header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

print page

title = []
link = []
for h3 in soup.find_all("h3", attrs={"class":"yt-lockup-title"}):
    title.append(h3.find('a').contents[0])
    link.append(h3.find('a')['href'])

print link

columns = ['S.No.', 'Title', 'Link']

table = PrettyTable(columns)

for i in range(len(title)):
    table.add_row([i+1, title[i], link[i]])

print table

if len(title) > 0:
    print "Enter your choice(numerical)"
    choice = raw_input()
    choice = int(choice)

    if 0 < choice <= len(title):
        video_url = "http://youtube.com" + link[choice-1]
        print video_url
        os.system("vlc " + video_url)
    else:
        print "Invalid Selection"
else:
    print "Sorry, no results found."

