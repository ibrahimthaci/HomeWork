from bs4 import BeautifulSoup
import requests

url = "https://kuvendikosoves.org/shq/deputetet/"
text = requests.get(url).text
soup = BeautifulSoup(text,'lxml') #or instead of lxml == html.parser
s = soup.find_all('h4', {'class':'name'})
for i in s:
    print(i)

#other way if we want to display without html tags
for s in soup.find_all('h4', {'class':'name'}):
    print(str(s)[17:][0:-5]) #you can eaisly use [17:-5] in same [] to remove before and after


    #or

url = "https://kuvendikosoves.org/shq/deputetet/"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')
p = soup.find_all('h4', {'class': 'name'})
for i in p:
    print(i)