'''
from bs4 import BeautifulSoup
import requests

url = "https://www.merriam-webster.com/dictionary/simultaneous"
data = requests.get(url)
soup = BeautifulSoup(data.text,'html.parser')  # to get html code.
# print(soup.prettify())
# print(soup)
print(soup.title)

'''

import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.tutorialsfreak.com")
soup = BeautifulSoup(web.content,"html.parser")
print(soup)
print("***********************************")
print(soup.prettify())


# Tag
tag = soup.html
print(tag)
print(type(tag))
tag = soup.p
print(tag)
tag = soup.a
print(tag)
rag = soup.h1
print(rag)
tag = soup.h2
print(tag)

# Navigable String
str = soup.p.string
print(str)
str1 = soup.h1.string
print(str1)

# BeautifulSoup
str = soup.body
print(str)

sr = soup.find("h1")
print(sr)

s = soup.find_all("h1")
print(s)

# Comments
com = soup.p.string
print(com)
