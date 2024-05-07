import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.tutorialsfreak.com")
print(url)
# print()
# print(url.content)
soup = BeautifulSoup(url.content,"html.parser")
print(soup.prettify())
# How to get elements from Web Page by class

class_data = soup.find("div",class_ = "scroll-top-home")
print(class_data)
